"""
Crie um programa que receba um número inteiro e exiba se ele é par ou ímpar.
"""

if __name__ == "__main__":

    numero = int(input("Informe um número: "))
    print("O número {} é {}".format(
        numero, "par" if numero % 2 == 0 else "ímpar"
    ))