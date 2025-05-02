import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pegamos o valor da variável de ambiente DATABASE_URL
connection_string = os.getenv("DATABASE_URL")

# Criamos a conexão com o banco de dados a partir da connection string. O parâmetro echo=True faz com que as consultas SQL que são executadas, sejam mostradas no terminal. Muito útil para depuração
connection = create_engine(
    url=connection_string,
    echo=True
)

# Agora vamor criar a sessão de acesso. É pela sessão que vamos executar os comandos. O parâmetro bind serve para associar a sessão a uma conexão, e o autoflush
session = scoped_session(sessionmaker(
    bind=connection
))

# A classe DeclarativeBase, é de onde todas as models serão herdadas. Para fins de padronização, criamos a classe Base que herda dela
class Base(DeclarativeBase):
    pass