from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# Criar a conexão à base de dados
db = create_engine("sqlite:///pizzaria.db")
# Permite trabalhar na base de dados
Base = declarative_base()
# Criar as classes/tabelas da base de dados
# Tabela Users
class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self,name,email,password,active=True,admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

# Tabela Orders
class Order(Base):
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user = Column("user", ForeignKey("users.id"), nullable=False) # ForeignKey - nome dado a tabela ponto seguido da chave primária da tabela
    status = Column("status", String) 
    price = Column("price", Float)
    # items = 

    def __init__(self,user,status="pending",price=0):
        self.user = user
        self.status = status
        self.price = price

# Tabela OrderItems
class OrdemItem(Base):
    __tablename__ = "order_items"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavour = Column("flavour", String)
    size = Column("size", String)
    unit_price = Column("unit_price", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self,quantity,flavour,size,unit_price,order):
        self.quantity = quantity
        self.flavour = flavour
        self.size = size
        self.unit_price = unit_price
        self.order = order

# Executar a criação dos metadados da sua base de dados
    # Executar pip install alembic para poder executar a migração das classes para tabelas da base de dados   
    # No terminal: alembic init alembic  
        # - O que faz? Cria uma pasta denominada alembic onde serão colocadas as nossas migrações
        # Cria um ficheiro alembic.ini onde estão as configurções do alembic
    # No ficheiro alembic.ini, alterar:
        # Atualizar o link da base de dados
    # No ficheiro env.py da pasta alembic:
        # Temos de importar a variável Base deste nosso ficheiro models.py
        # Código abaixo
            # import sys
            # import os
            # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
        # Agora ainda no env.p, antes da linha target_metadata = None, fazer:
            # from models import Base
            # target_metadata = Base.metadata
    # Criar o ficheiro de migração (no terminal)
        # alembic revision --autogenerate -m "Initial migration"
        # Nota: Não utilizar acentos na mensagem da migração
        # Notar que ele cria dentro da pasta versions o ficheiro de migração
    # Executar a migração (no terminal)
        # alembic upgrade head

# Este passo cria efetivamente a base de dados