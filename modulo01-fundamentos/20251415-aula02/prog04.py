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

    # Atualizando um dicionário (Modificando, adicionando e removendo itens)
    # Podemos atualizar um dicionário de diferentes maneiras

    # Abaixo estamos inserindo um novo par chave: valor (tipo_sanguineo = A+) e atualizando o valor da chave "idade" para 25
    jose["tipo_sanguineo"] = "A+"
    jose["idade"] = 25
    print(jose)

    # Podemos ter o mesmo resultado utilizando o método update()
    joao.update({"tipo_sanguineo": "B-"})
    joao.update({"idade": 28})
    print(joao)

    # Vamos inserir mais 2 pares chave: valor
    joao.update({"genero": "M", "status": "Solteiro"})

    # Agora vamos remover essas chaves criadas. Podemos utilizar 2 métodos para isso:

    # O método pop remove um par chave: valor de acordo com o nome da chave
    print(joao)
    print(joao.pop("status"))

    # O método popitem() remove o último par chave: valor inserido
    # Remove o par genero: M
    joao.popitem()
    print(joao)

    print('*' * 20, " LAÇO FOR ", '*' * 20)

    # Iterando sobre dicionários utilizando for loop

    for item in joao:
        print(item)

    # Por padrão, o laço for retorna as chaves do dicionário (internamente chama o método keys()). Porém, podemos utilizar alguns métodos para retornar os valores ou até mesmo os pares chave: valor

    # Se queremos apenas os valores do dicionário, utilizamos o método values()
    for item in joao.values():
        print(item)

    # Finalmente, o método items() retorna o par chave: valor como uma tupla
    for chave, valor in jose.items():
        print("{}: {}".format(chave, valor))

    print('*' * 20, " CÓPIA DE DICIONÁRIOS ", '*' * 20)
    

    # Cópia de dicionários
    # Dicionários seguem o mesmo princípio de listas: São variáveis que apontam pra uma posição de memória, e que caso sejam igualadas, podem alterar o valor uma da outra. Pra contornar isso, podemos utilizar o método copy ou a função dict()

    joaozinho = joao.copy()
    joaozinho.update({"nome": "João Júnior", "idade": 8, "tipo_sanguineo": "O"})
    print(joao, joaozinho)

    zezinho = dict(jose)
    zezinho.update({"nome": "José Júnior", "idade": 7, "tipo_sanguineo": "O+"})
    print(jose, zezinho)

    # Limpando os dicionários
    joao.clear()
