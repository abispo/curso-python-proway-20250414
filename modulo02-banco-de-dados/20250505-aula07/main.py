from config import connection, Base
from mensagens import MENU_PRINCIPAL
from models import *
from postagens import gerenciar_postagens
from usuarios import gerenciar_usuarios

if __name__ == "__main__":
    # Como estamos utilizando o alembic para controlar as alterações no nosso banco de dados, a linha abaixo não é mais necessária
    # Base.metadata.create_all(connection)

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
                gerenciar_postagens()

            case 4:
                pass
            
            case 5:
                pass

            case _:
                print(f"Opção '{opcao}' inválida.")