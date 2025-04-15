"""
Escreva um programa que solicite o nome, a idade e o gênero do usuário. Em seguida, exiba uma mensagem personalizada informando se o gênero é masculino ou feminino e se é maior ou menor de idade.
"""

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    genero = input("Informe o seu gênero(M ou F): ")
    idade = int(input("Informe a sua idade: "))

    mensagem = """
    Olá {}!
    Você é do gênero {}.
    E você é {} de idade.
    """.format(
        nome,
        "Masculino" if genero == "M" else "Feminino",
        "maior" if idade >= 18 else "menor"
    )
    
    print(mensagem)
