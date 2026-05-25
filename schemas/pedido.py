from pydantic import BaseModel

class ObservacaoInput(BaseModel):
    observacao: str

class PedidoFilaOut(BaseModel):
    codigo: int
    cpf: str
    prioritario: bool
    observacao: str