"""
Escreva um programa que leia três números inteiros e exiba o maior e o menor deles.
"""

if __name__ == "__main__":

    # Nesse caso, iremos utilizar as funções built-in min() e max(), que retornam o manor e o maior valor de um iterável, respectivamente.

    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    n3 = float(input("Informe o terceiro número: "))

    menor_numero = min(n1, n2, n3)
    maior_numero = max(n1, n2, n3)

    print(f"O menor número informado é {menor_numero}.")
    print(f"O maior número informado é {maior_numero}.")