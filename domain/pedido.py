class Pedido:
    def __init__(self, cliente: str, produtos: list):
        self.cliente = cliente
        self.produtos = produtos
        self.entregue = False
        
        self.esta_cancelado = False
        self.prioritario = False
        self.observacao = ""

    def cancelar(self) -> bool:
        if self.entregue or self.esta_cancelado:
            return False
        
        self.esta_cancelado = True
        return True

    def adicionar_observacao(self, observacao: str) -> bool:
        if self.entregue:
            return False
        
        if not observacao or observacao.strip() == "":
            return False
            
        if len(observacao) > 200:
            return False
            
        self.observacao = observacao.strip()
        return True

    def tornar_prioritario(self) -> bool:
        if self.esta_cancelado or self.entregue:
            return False
            
        self.prioritario = True
        return True