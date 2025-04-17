"""
Funções (ou Procedures)

Também podemos passar valores para as funções, valores esses que serão acessados dentro delas. Para isso utilizamos os parâmetros
"""

from utils import lista_pesos_e_alturas, dicionarios_pesos_e_alturas

# Abaixo indicamos 2 parâmetros: peso e altura
def calculo_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura)

if __name__ == "__main__":

    print(f"{calculo_imc(113.8, 1.96):.1f}")
    # Acima, passamos os valores para a função de maneira posicional, ou seja, o primeiro valor será atribuído ao parâmetro peso, e o segundo valor será atribuído ao parâmetro altura. Perceba que se passarmos os valores invertidos, nosso cálculo terá um resultado diferente.

    # A segunda maneira de passar valores para uma função é especificando explicitamente o nome do parâmetro que receberá o valor. Dessa maneira, não precisamos respeitar a ordem dos parâmetros definidos na função.

    print(calculo_imc(peso=77, altura=1.65))
    print(calculo_imc(altura=1.80, peso=94))

    # Imagine o cenário onde precisamos calcular os valores de peso e altura de uma lista de tuplas. Podemos fazer isso de 2 maneiras utilizando a função calculo_imc

    print('*' * 20, "Desempacotamento de valores", '*' * 20)

    for item in lista_pesos_e_alturas:
        peso = item[0]
        altura = item[1]

        print(f"{calculo_imc(peso, altura):.1f}")

    # Abaixo podemos utilizar a sintaxe * onde podemos passar vários parâmetro de uma vez só para a função

    for item in lista_pesos_e_alturas:
        print(f"{calculo_imc(*item):.1f}")

    # Também podemos utilizar a mesma abordagem para dicionários:
    for item in dicionarios_pesos_e_alturas:
        print(f"{calculo_imc(**item):.1f}")
