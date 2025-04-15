# Operadores em Python

# Operadores de comparação

from random import randint

if __name__ == "__main__":

    numero = randint(1, 100)

    if numero < 5:
        print("Número muito baixo")

    elif numero < 20 and numero < 50:
        print("Número baixo")

    elif numero >= 51 and numero < 80:
        print("Número alto")

    else:
        print("Número muito alto")