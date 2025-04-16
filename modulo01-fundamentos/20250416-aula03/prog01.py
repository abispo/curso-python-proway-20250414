"""
Funções (ou Procedures)

De maneira simples, funções são blocos de código que executam determinada tarefa. Como são blocos de código independentes, podemos reutilizar essas funções em quaisquer lugares do nosso código. Funções podem também receber valores por meio de parâmetros, e retornar qualquer tipo de valor.
"""

from datetime import datetime

def hello():
    print("Olá!")

def data_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if __name__ == "__main__":
    hello()
    print(data_atual())