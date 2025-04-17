"""
Funções (ou Procedures)

Funções recursivas

Uma função recursiva basicamente é uma função que chama a si mesma. Devido a sua natureza, precisamos tomar cuidado ao implementar esse tipo de função, pois caso não haja uma lógica pare retorno dessa função, ela será chamada indefinidamente, até gerar uma exceção.

Um exemplo clássico de função recursiva é a função fatorial
5! = 5 * 4 * 3 * 2 * 1
"""

def fatorial_nao_recursivo(numero: int) -> int:
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador = contador - 1

    return total

def fatorial_recursivo(numero: int) -> int:

    if numero == 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)


if __name__ == "__main__":
    print(fatorial_nao_recursivo(10))
    print(fatorial_recursivo(5))