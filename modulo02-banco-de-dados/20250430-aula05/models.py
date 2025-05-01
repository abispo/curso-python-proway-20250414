"""
Uma model nada mais é do que uma classe que está sendo mapeada para uma tabela no banco de dados. Ou seja, é a representação dessa tabela como uma classe. Os atributos dessa classe são mapeados para os nomes das colunas da tabela, ou seja, além dos nomes, devem ter o mesmo tipo.

Nesse projeto, iremos criar a mesma estrutura de tabelas que criamos no na aula 2 do módulo de banco de dados (tabelas e seus relacionamentos)
"""
import datetime
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from config import Base

# Aqui criamos a classe Usuario, que herda da classe Base. Obrigatoriamente, todas as models devem herdar da classe DeclarativeBase. Como Base herda dela, então Usuario também herda. Chamamos essa classe mapeada de Model
class Usuario(Base):

    # O atributo __tablename__ será utilizado para definir o nome da tabela no banco de dados.
    __tablename__ = "usuarios"

    # Abaixo, estamos criando os atributos da classe, que serão mapeados para as colunas da tabela. Precisamos indicar o tipo, e outras características, como chave primária, nulável, etc.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    senha: Mapped[str] = mapped_column(String(100), nullable=False)

    def __str__(self):
        return f"<Usuario({self.email})>"
    
    def __repr__(self):
        return f"<Usuario({self.email})>"


class Perfil(Base):

    __tablename__ = "perfis"

    # A classe ForeignKey, indica que essa coluna na tabela será uma chave estrangeira da coluna 'id' da tabela 'usuarios'.
    id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    data_de_nascimento: Mapped[datetime.date] = mapped_column(Date)

    def __str__(self):
        return f"<Perfil({self.nome})>"
    
    def __repr__(self):
        return f"<Perfil({self.nome})>"