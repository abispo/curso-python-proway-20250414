"""
Faça um programa que receba uma temperatura em graus Celsius e exiba a temperatura equivalente em graus Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.
"""

if __name__ == "__main__":

    temperatura_celsius = float(input("Informe a temperatura em graus celsius: "))
    temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32

    print("{}ºC equivalem a {}ºF.".format(temperatura_celsius, temperatura_fahrenheit))