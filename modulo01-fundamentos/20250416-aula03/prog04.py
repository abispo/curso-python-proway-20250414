"""
Funções (ou Procedures)

Empacotamento do parâmetros.
"""

def calculo_media(*args):
    return sum(args) / len(args)

def mostrar_info_usuario(**kwargs):
    print('*'*30)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":

    # Imagine que você leia dados de alguma fonte, onde o número de dados recebidos não é exato
    print(f"{calculo_media(5, 3, 7, 8, 9, 8, 7):.1f}")
    print(f"{calculo_media(5, 7):.1f}")
    print(f"{calculo_media(1):.1f}")
    print(f"{calculo_media(5.6, 3.1, 7.6, 8, 9, 8, 7):.1f}")
    print(f"{calculo_media(5.7):.1f}")

    maria = {
        "nome": "Maria", "idade": 40, "cidade": "Blumenau"
    }
    joao = {
        "nome": "João", "cidade": "Indaial"
    }
    joana = {
        "nome": "Joana", "estado_civil": "Solteira"
    }

    mostrar_info_usuario(**maria)
    mostrar_info_usuario(**joao)
    mostrar_info_usuario(**joana)