"""
Crie um programa que peça ao usuário para digitar dois números inteiros e exiba a soma, subtração, multiplicação e divisão dos números.
"""

if __name__ == "__main__":

    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))

    print("{} + {} = {}".format(n1, n2, n1 + n2))
    print("{} - {} = {}".format(n1, n2, n1 - n2))
    print("{} * {} = {}".format(n1, n2, n1 * n2))
    print("{} / {} = {}".format(n1, n2, n1 / n2))