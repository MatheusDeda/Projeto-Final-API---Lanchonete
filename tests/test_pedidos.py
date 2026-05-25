import pytest
from domain.pedido import Pedido
from services.lanchonete_service import LanchoneteService

# --- TESTES DE DOMÍNIO (Regras do Pedido) ---

def test_deve_cancelar_pedido():
    pedido = Pedido(cliente="12345678900", produtos=["Hamburguer", "Refri"])
    resultado = pedido.cancelar()
    
    assert resultado is True
    assert pedido.esta_cancelado is True

def test_nao_deve_cancelar_pedido_entregue():
    pedido = Pedido(cliente="12345678900", produtos=["Hamburguer"])
    pedido.entregue = True  # Simulando que o pedido já saiu da cozinha
    
    resultado = pedido.cancelar()
    
    assert resultado is False
    assert pedido.esta_cancelado is False

def test_deve_adicionar_observacao():
    pedido = Pedido(cliente="12345678900", produtos=["Pizza"])
    resultado = pedido.adicionar_observacao("Sem cebola e sem borda recheada")
    
    assert resultado is True
    assert pedido.observacao == "Sem cebola e sem borda recheada"

def test_nao_deve_aceitar_observacao_vazia():
    pedido = Pedido(cliente="12345678900", produtos=["Pizza"])
    resultado_vazio = pedido.adicionar_observacao("")
    resultado_espacos = pedido.adicionar_observacao("   ")
    
    assert resultado_vazio is False
    assert resultado_espacos is False
    assert pedido.observacao == ""

def test_deve_tornar_pedido_prioritario():
    pedido = Pedido(cliente="12345678900", produtos=["Batata Frita"])
    resultado = pedido.tornar_prioritario()
    
    assert resultado is True
    assert pedido.prioritario is True


# --- TESTES DE SERVIÇO (Regras da Fila de Preparo) ---

def test_fila_deve_ter_prioritarios_primeiro():
    # Cria três pedidos simulando a ordem de chegada
    pedido1 = Pedido(cliente="CPF-1", produtos=["Agua"])
    pedido2 = Pedido(cliente="CPF-2", produtos=["Suco"])
    pedido3 = Pedido(cliente="CPF-3", produtos=["Bolo"])
    
    # O pedido 3 chegou por último, mas será marcado como prioritário
    pedido3.tornar_prioritario()
    
    db_simulado = {1: pedido1, 2: pedido2, 3: pedido3}
    service = LanchoneteService(db_pedidos=db_simulado)
    
    fila = service.listar_fila_preparo()
    
    # Valida se a fila tem 3 itens e se o código 3 foi movido para o topo
    assert len(fila) == 3
    assert fila[0]["codigo"] == 3
    assert fila[0]["prioritario"] is True
    # Valida se a ordem dos outros pedidos normais foi mantida
    assert fila[1]["codigo"] == 1
    assert fila[2]["codigo"] == 2

def test_fila_nao_deve_listar_cancelados():
    pedido1 = Pedido(cliente="CPF-1", produtos=["Agua"])
    pedido2 = Pedido(cliente="CPF-2", produtos=["Suco"])
    
    # Cancela o pedido 1
    pedido1.cancelar()
    
    db_simulado = {1: pedido1, 2: pedido2}
    service = LanchoneteService(db_pedidos=db_simulado)
    
    fila = service.listar_fila_preparo()
    
    # A fila deve ignorar o pedido 1 (cancelado) e mostrar apenas o pedido 2
    assert len(fila) == 1
    assert fila[0]["codigo"] == 2