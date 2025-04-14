# Tipos de dados

# Tipos numéricos
# No Python, temos 3 tipos de dados numéricos: int(inteiro), float(numero com casa decimal) e complex(números complexos)

if __name__ == "__main__":

    # Quando estamos trabalhando com tipos numéricos e recebemos valores pelo terminal, precisamos converter esse valor para inteiro, pois a função input() sempre retorna strings.
    # Chamamos esse processo de conversão entre tipos de cast
    numero1 = input("Informe o primeiro número: ")
    numero2 = input("Informe o segundo número: ")

    soma = int(numero1) + int(numero2)

    print("A soma de {} e {} é igual a {}".format(
        numero1, numero2, soma
    ))

    print(2/5)
    print(float(10))

    print(f"{5.184982792728094127492847218904754908527534892:.2f}")