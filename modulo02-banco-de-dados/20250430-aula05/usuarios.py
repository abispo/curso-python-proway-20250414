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
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case _:
                print(f"Opção '{opcao}' inválida")