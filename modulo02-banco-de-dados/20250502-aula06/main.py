from config import connection, Base
from mensagens import MENU_PRINCIPAL
from models import *
from usuarios import gerenciar_usuarios

if __name__ == "__main__":
    Base.metadata.create_all(connection)

    while True:
        
        print(MENU_PRINCIPAL)
        opcao = int(input("Informe a opção escolhida: "))

        match opcao:
            case 1:
                print("Você escolheu 'SAIR'.")
                break

            case 2:
                gerenciar_usuarios()

            case 3:
                pass

            case 4:
                pass
            
            case 5:
                pass

            case _:
                print(f"Opção '{opcao}' inválida.")