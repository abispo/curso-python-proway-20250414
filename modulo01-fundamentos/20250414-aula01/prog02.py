# Tipos de dados em Python

# Tipo texto (str)
# Variáveis do tipo str em Python armazenam cadeiras de caracteres, independentemente de quais caracteres sejam

if __name__ == "__main__":

    print("Podemos criar strings com aspas duplas")
    print('Podemos criar strings com aspas simples')
    print("Podemos 'misturar' uma com a outra.")
    print("Podemos utilizar \"caracteres especiais\" se quisermos.")

    mensagem = """

        Podemos utilizar também strings multi-linha, ou seja, strings que não são limitadas pelo fim de uma linha. Muito úteis para criação de menus, documentação de funções, etc
    """
    print(mensagem)

    # Podemos utilizar algumas maneiras para concatenar strings, para os mais variados fins.

    # Maneira "antiga"
    curso = "Python"
    print("Bem vindo ao curso de %s" % curso)
    # O caractere %s está sendo substituído pelo valor da variável 'curso'

    # Maneira moderna 1
    curso = "Java"
    print("Bem vindo ao curso de {}, {}".format(curso, "Amanda"))
    # Como tudo em Python são objetos, podemos utilizar os métodos desses objetos. No caso acima, estamos utilizando o método format() para substituir o conjunto de chaves ({}) pelos valores passados para o método, na ordem em que aparecem.
