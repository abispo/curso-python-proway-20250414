"""
Crie um programa que receba o nome, o peso e a altura de uma pessoa. Em seguida, calcule o seu IMC. A altura deve ser informada no formato metros.centimetros (exemplo 1.79). A fórmula do IMC é a seguinte: peso / (altura * altura).
"""

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    peso = float(input("Informe o seu peso em Kg: "))
    altura = float(input("Informe a sua altura (m.c): "))

    imc = peso / (altura * altura)

    print("{}, seu peso é de {} e sua altura é de {}. Seu IMC é de {:.1f}".format(
        nome, peso, altura, imc
    ))
