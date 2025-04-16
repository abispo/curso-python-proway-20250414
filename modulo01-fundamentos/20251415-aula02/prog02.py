"""
Laços de repetição

Um laço de repetição basicamente é um comando que executa um bloco de código enquanto uma determinada condição é verdadeira. O Python possui 2 estruturas que fazem isso: Os laços for e while

Laço while

O laço while é utilizando quando precisamos executar um bloco de código repetidas vezes, enquanto uma condição é verdadeira.
"""

if __name__ == "__main__":

    lista_de_compras = []           # Podemos também utilizar list()
    continuar_executando = True

    while continuar_executando:

        mensagem = """
        CADASTRO DE ITENS
        OPCOES:

        C - CADASTRAR ITEM NA LISTA
        D - REMOVER ITEM DA LISTA
        U - REMOVER ÚLTIMO ITEM ADICIONADO NA LISTA
        S - MOSTRAR ITENS DA LISTA
        X - SAIR

        """
        print(mensagem)
        opcao = input("Informe a opção escolhida")

        match opcao.upper():
            case "X":
                print("Saindo...")
                break   # break é uma instrução que interrompe automaticamente a execução do loop, tanto faz o for loop ou o while loop

            case "C":
                item = input("Informe o item: ")
                lista_de_compras.append(item)

            # Caso padrão. Caso nenhuma das verificações anteriores forem satisfeitas, o bloco abaixo é executado
            case _:
                print("Opção desconhecida")