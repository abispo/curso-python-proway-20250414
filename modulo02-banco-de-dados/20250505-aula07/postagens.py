from sqlalchemy import select

from config import session
from mensagens import MENU_POSTAGENS
from models import Usuario, Postagem, Categoria

def gerenciar_postagens():
    
    while True:
        print(MENU_POSTAGENS)
        opcao = int(input("Informe a opção escolhida: "))

        match opcao:
            case 1:
                break

            case 2:
                cadastrar_postagem()

            case 3:
                selecionar_postagens()

            case 4:
                atualizar_postagem()

            case 5:
                apagar_postagem()

            case _:
                print(f"Opção '{opcao}' inválida")


def cadastrar_postagem():

    email = input("Informe o e-mail do usuário: ")

    consulta = select(Usuario).where(Usuario.email == email)
    usuario = session.scalars(consulta).one_or_none()

    if not usuario:
        print(f"O usuário '{email}' não foi encontrado.")
        return

    titulo = input("Informe o título da postagem: ")
    texto = input("Informe o texto da postagem: ")
    lista_categorias = input("Informe as categorias dessa postagem (separadas por vírgula): ").replace(
        " ", ""
    ).split(",")

    categorias = []
    for item_categoria in lista_categorias:
        categoria = session.scalars(select(Categoria).where(Categoria.nome == item_categoria)).one_or_none()
        
        if not categoria:
            categoria = Categoria(nome=item_categoria)
            session.add(categoria)
            session.commit()
        
        categorias.append(categoria)

   
    postagem = Postagem(usuario=usuario, titulo=titulo, texto=texto, categorias=categorias)
    session.add(postagem)
    session.commit()

    print(f"A Postagem '{postagem.titulo}' foi cadastrada com sucesso!")

def selecionar_postagens():
    pass


def atualizar_postagem():
    pass


def apagar_postagem():
    pass