class LanchoneteService:
    def __init__(self, db_pedidos: dict = None):
        if db_pedidos is None:
            db_pedidos = {}
        self.db = db_pedidos

    def cancelar_pedido(self, cod_pedido: int):
        if cod_pedido not in self.db:
            raise KeyError("Pedido não encontrado.")
            
        pedido = self.db[cod_pedido]
        
        if not pedido.cancelar():
            raise ValueError("O pedido não pode ser cancelado (já entregue ou previamente cancelado).")
            
        return pedido

    def adicionar_observacao(self, cod_pedido: int, observacao: str):
        if cod_pedido not in self.db:
            raise KeyError("Pedido não encontrado.")
            
        pedido = self.db[cod_pedido]
        
        if not pedido.adicionar_observacao(observacao):
            raise ValueError("Observação inválida, muito longa ou pedido já entregue.")
            
        return pedido

    def tornar_pedido_prioritario(self, cod_pedido: int):
        if cod_pedido not in self.db:
            raise KeyError("Pedido não encontrado.")
            
        pedido = self.db[cod_pedido]
        
        if not pedido.tornar_prioritario():
            raise ValueError("Pedido não pode ser priorizado pois não está ativo na fila.")
            
        return pedido

    def listar_fila_preparo(self):
        fila_ativa = []
        
        for codigo, pedido in self.db.items():
            if not pedido.esta_cancelado and not pedido.entregue:
                fila_ativa.append({
                    "codigo": codigo,
                    "cpf": pedido.cliente, 
                    "prioritario": pedido.prioritario,
                    "observacao": pedido.observacao
                })
                
        fila_ordenada = sorted(fila_ativa, key=lambda p: p["prioritario"], reverse=True)
        return fila_ordenada