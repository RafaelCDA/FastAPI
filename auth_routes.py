from fastapi import APIRouter, Depends
from models import Usuario
from dependences import pegar_sessao

auth_router = APIRouter(prefix= "/auth", tags= ["auth"])

@auth_router.get("/")

async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return{"Mensagem": "Você acessou a rota de autenticação", "Autenticado" : "False"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str,nome : str, session = Depends(pegar_sessao()) ):

    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"Mensagem": "ja existe"}
    else:
        novo_usuario = Usuario(nome,email,senha)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem":"usuario cadastrado com sucesso"}