"""
Funções (ou Procedures)

De maneira simples, funções são blocos de código que executam determinada tarefa. Como são blocos de código independentes, podemos reutilizar essas funções em quaisquer lugares do nosso código. Funções podem também receber valores por meio de parâmetros, e retornar qualquer tipo de valor.
"""

from datetime import datetime

# Utilizamos a palavra reservada def para criar uma função
# A função abaixo apenas exibe uma mensagem no terminal
def hello():
    print("Olá!")

# A função abaixo chama o método now() da classe datetime e formata a saída em dia/mes/ano hora:minuto:segundo
def data_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if __name__ == "__main__":
    hello()
    print(data_atual())

    # Abaixo o que será impresso será o endereço de memória dessa função, e não o valor retornado.
    print(data_atual)