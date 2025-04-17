"""
Funções (ou Procedures)

Funções lambda

No Python, chamamos as funções anônimas de funções lambda. Como o próprio no já diz, funções anônimas são funções que não possuem nome. Geralmente utilizamos essas funções como parâmetros de outras funções.
"""

def so_impares(numero):
    return numero % 2 == 1

if __name__ == "__main__":

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lista_impares = filter(lambda x: x % 2 == 0, lista)
    print(list(lista_impares))