from fastapi import APIRouter
from models import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Criar um rota no FastAPI
@auth_router.get("/") # http://127.0.0.1:8000/auth/
async def home():
    return { "message": "You have just accessed the auth routes." }

@auth_router.post("/register")
async def register(name: str, email: str,password: str):
    # Se o utilizador não enviar ums string, o FastAPI tem um processo para indicação de erro
    # Existe um limite de conexão à base de dados
    # É importante ao abrir uma sessão (conectar à bd), lembrar de fechar a sessão
    Session = sessionmaker(bind=db) # Criar uma sessão na base de dados
    session = Session() # Criar uma instância da sessão, ou seja, conectar à base de dados
    user = session.query(User).filter(User.email==email).first() # Consulta SQL 

    if user:
        return { "message": "An user with this email address already registeres"}
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return { "message": "User registered with success" }
# O código desta função tem vários problemas
    # Não há fecho da sessão
    # Não há garantia que o commit é executado completamente
    # Falta o HTTP Code Status dos retornos
    # Password não está criptografada
    # Não é um erro, mas a função devia receber como parâmetro uma instância de User e não "dados soltos"
# Testar o código no FastApi (Rota docs)