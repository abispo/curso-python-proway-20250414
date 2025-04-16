"""
Laços de repetição

Um laço de repetição basicamente é um comando que executa um bloco de código enquanto uma determinada condição é verdadeira. O Python possui 2 estruturas que fazem isso: Os laços for e while

Laço for

O laço for é utilizado quando precisamos iterar sobre uma sequência. Ele irá ler os itens de maneira sequencial, até não existirem mais itens a serem lidos.
"""

if __name__ == "__main__":

    curso = "Python"
    for letra in curso:
        print(letra)

    
    for indice, valor in enumerate(curso):
        print("{} - {}".format(indice, valor))