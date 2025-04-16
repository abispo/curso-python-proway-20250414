"""
Dicionários em Python

Dicionários são estruturas de dados que armazenam os dados em um formato chave: valor. Esse tipo de estrutura é bastante utilizada quando trabalhamos com tipos de dados json.

Dicionários são mutáveis, iteráveis e não permitem chaves com o mesmo valor
"""

if __name__ == "__main__":

    # Criação de um dicionário
    jose = {"nome": "José", "idade": 20}
    joao = dict(nome="João", idade=30)
    vazio = {}      # dict()

    print(jose, joao)

    # Um valor associado a uma chave, pode ser de qualquer tipo de dados, inclusive outros dicionários. Não existe limitação. Porém, uma chave de dicionário é limitada a ter determinados tipos de valor, como: string, numeros e valores booleanos

    # Acessando itens de um dicionário
    # Existem 2 maneiras de acessar os valores de um dicionário:

    # Acessando diretamente o nome da chave
    print("A idade de {} é {}.".format(jose["nome"], jose["idade"]))

    # Com esse método, apenas precisamos tomar cuidado ao acessar a chave, pois ela deve existir. Se tentarmos acessar o valor de uma chave que não existe, a exceção KeyError será lançada. A linha abaixo gerará um erro.
    # print(jose["tipo_sanguineo"])

    # Também podemos acessar o valor de um dicionário, utilizando o método get()
    print("A idade de {} é {}.".format(joao.get("nome"), joao.get("idade")))

    # Nesse caso, ao invés de ser lançada a exceção KeyError, o método get irá retornar None
    print(joao.get("tipo_sanguineo"))

    # Caso queiramos retornar um valor padrão ao invés do nome, passamos como segundo parâmetro da função.
    print(joao.get("tipo_sanguineo", "A chave 'tipo_sanguineo' não existe"))

    # Atualizando um dicionário

    # Adicionando e removendo itens de um dicionário

    # Iterando sobre dicionários utilizando for loop

    # Cópia de dicionários