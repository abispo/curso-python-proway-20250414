"""
Uma model nada mais é do que uma classe que está sendo mapeada para uma tabela no banco de dados. Ou seja, é a representação dessa tabela como uma classe. Os atributos dessa classe são mapeados para os nomes das colunas da tabela, ou seja, além dos nomes, devem ter o mesmo tipo.

Nesse projeto, iremos criar a mesma estrutura de tabelas que criamos no na aula 2 do módulo de banco de dados (tabelas e seus relacionamentos)
"""
from typing import List
import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import Base

postagens_categorias = Table(
    "postagens_categorias",
    Base.metadata,
    Column("postagem_id", ForeignKey("postagens.id"), primary_key=True),
    Column("categoria_id", ForeignKey("categorias.id"), primary_key=True)
)

# Aqui criamos a classe Usuario, que herda da classe Base. Obrigatoriamente, todas as models devem herdar da classe DeclarativeBase. Como Base herda dela, então Usuario também herda. Chamamos essa classe mapeada de Model
class Usuario(Base):

    # O atributo __tablename__ será utilizado para definir o nome da tabela no banco de dados.
    __tablename__ = "usuarios"

    # Abaixo, estamos criando os atributos da classe, que serão mapeados para as colunas da tabela. Precisamos indicar o tipo, e outras características, como chave primária, nulável, etc.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    senha: Mapped[str] = mapped_column(String(100), nullable=False)
    criado_em: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now(datetime.UTC),
        nullable=True
    )
    atualizado_em: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
        nullable=True
    )

    # Aqui criamos um atributo do tipo relationship. Esse atributo existirá apenas em tempo de execução, ou seja, ele não será criado fisicamente na tabela de usuarios. Criando esse atributo, é possível fazer a chamada usuario.perfil.nome. 
    perfil: Mapped["Perfil"] = relationship(back_populates="usuario")
    postagens: Mapped[List["Postagem"]] = relationship(back_populates="usuario")
    comentarios: Mapped[List["Comentario"]] = relationship(back_populates="usuario")

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

    # A mesma coisa que Usuario, porém aqui estamos criando o atributo usuario na entidade Perfil.
    usuario: Mapped["Usuario"] = relationship(back_populates="perfil")

    def __str__(self):
        return f"<Perfil({self.nome})>"
    
    def __repr__(self):
        return f"<Perfil({self.nome})>"
    

class Postagem(Base):

    __tablename__ = "postagens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    texto: Mapped[str] = mapped_column(String(300), nullable=False)
    criado_em: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now(datetime.UTC)
    )

    usuario: Mapped["Usuario"] = relationship(back_populates="postagens")
    categorias: Mapped[List["Categoria"]] = relationship(back_populates="postagens", secondary=postagens_categorias)
    comentarios: Mapped[List["Comentario"]] = relationship(back_populates="postagem")

    def __str__(self):
        return f"<Postagem({self.titulo})>"
    
    def __repr__(self):
        return f"<Postagem({self.titulo})>"
    

class Categoria(Base):

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    postagens: Mapped[List["Postagem"]] = relationship(back_populates="categorias", secondary=postagens_categorias)

    def __str__(self):
        return f"<Categoria({self.nome})>"
    
    def __repr__(self):
        return f"<Categoria({self.nome})>"
    

class Comentario(Base):

    __tablename__ = "comentarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    postagem_id: Mapped[int] = mapped_column(Integer, ForeignKey("postagens.id"), nullable=False)
    texto: Mapped[str] = mapped_column(String(200), nullable=False)
    criado_em: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC)
    )

    usuario: Mapped["Usuario"] = relationship(back_populates="comentarios")
    postagem: Mapped["Postagem"] = relationship(back_populates="comentarios")

    def __str__(self):
        return f"<Comentario({self.texto[:50]}...)>"
    
    def __repr__(self):
        return f"<Comentario({self.texto[:50]}...)>"
