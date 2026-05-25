from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from schemas.pedido import ObservacaoInput, PedidoFilaOut
from services.lanchonete_service import LanchoneteService

router = APIRouter(prefix="/lanchonete/pedidos", tags=["Pedidos"])

_db_pedidos_memoria = {}

def get_lanchonete_service() -> LanchoneteService:
    return LanchoneteService(db_pedidos=_db_pedidos_memoria)

@router.get("/fila/preparo", response_model=List[PedidoFilaOut], status_code=status.HTTP_200_OK)
def listar_fila_preparo(service: LanchoneteService = Depends(get_lanchonete_service)):
    return service.listar_fila_preparo()

@router.post("/{cod_pedido}/observacao", status_code=status.HTTP_200_OK)
def adicionar_observacao(
    cod_pedido: int,
    payload: ObservacaoInput,
    service: LanchoneteService = Depends(get_lanchonete_service)
):
    try:
        service.adicionar_observacao(cod_pedido, payload.observacao)
        return {"mensagem": "Observação adicionada com sucesso."}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/{cod_pedido}/cancelar", status_code=status.HTTP_200_OK)
def cancelar_pedido(
    cod_pedido: int,
    service: LanchoneteService = Depends(get_lanchonete_service)
):
    try:
        service.cancelar_pedido(cod_pedido)
        return {"mensagem": "Pedido cancelado com sucesso."}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/{cod_pedido}/prioridade", status_code=status.HTTP_200_OK)
def tornar_pedido_prioritario(
    cod_pedido: int,
    service: LanchoneteService = Depends(get_lanchonete_service)
):
    try:
        service.tornar_pedido_prioritario(cod_pedido)
        return {"mensagem": "Pedido atualizado para prioritário com sucesso."}
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))