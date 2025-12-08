from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos",tags=["pedidos"])

@order_router.get("/")

async def pedidos():
    """
       Essa é a rota padrão de pedidos do sistema
       """
    return{"Mensagem":"Você acessou a rota de pedidos"}