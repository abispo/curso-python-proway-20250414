from datetime import datetime

from sqlalchemy import select

from config import session
from mensagens import MENU_USUARIOS
from models import Usuario, Perfil

def gerenciar_usuarios():
    
    while True:
        print(MENU_USUARIOS)
        opcao = int(input("Informe a opção escolhida: "))

        match opcao:
            case 1:
                break

            case 2:
                cadastrar_usuario()

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case _:
                print(f"Opção '{opcao}' inválida")


def cadastrar_usuario():

    # Pedimos as informações de usuário
    email = input("Informe o e-mail do usuário: ")
    senha = input("Informe a senha do usuário: ")
    nome = input("Informe o nome do usuário: ")
    data_de_nascimento = input("Informe a data de nascimento (dd/mm/yyyy)")

    # Instanciamos a classe Usuario passando o e-mail e a senha
    usuario = Usuario(email=email, senha=senha)

    # Adicionamos esse objeto na sessão. Ele ficará "enfileirado", até confirmarmos a transação
    session.add(usuario)

    # Confirmamos a transação com o commit(). Todas as operações que estiverem pendentes na sessão, serão executadas
    session.commit()

    # A partir de usuario, criamos o perfil desse usuario
    perfil = Perfil(
        id=usuario.id,
        nome=nome,
        data_de_nascimento=datetime.strptime(
            data_de_nascimento, "%d/%m/%Y"      # Aqui convertemos a string em uma data
        ).date()
    )

    # Adicionamos o perfil à sessão e depois confirmamos a transação
    session.add(perfil)
    session.commit()

    print(f"Usuário {perfil.nome}({usuario.email}) cadastrado com sucesso!")