"""
Listas em Python (parte 2)

Métodos, list-comprehension, slice e cópia de listas
"""

if __name__ == "__main__":

    itens = ["Cupim", "Picanha", "Costela", "Maminha", "Linguiça"]
    #           0         1           2         3           4
    # Cada item da lista possui um índice, sempre começando por 0. Ou seja, se quisermos acessar individualmente um item de uma lista, passamos o seu índice.

    # Exemplo: Acessando o terceiro item da lista (índice 2)
    print(itens[2])

    # Devemos porém tomar cuidado, pois caso o índice informado não exista, será gerada uma exceção do tipo IndexError: list index out of range
    # print(itens[5])

    # Também conseguimos utilizar índices negativos, com o -1 começando pelo último item da lista:

    # ["Cupim", "Picanha", "Costela", "Maminha", "Linguiça"]
    #     -5        -4         -3         -2         -1
    print(itens[-1])

    # A partir dos índices de uma lista, podemos utilizar o recurso de slicing (ou fatiamento) de sequencias (Listas, strings, etc)

    # Primeiro vamos adicionar mais itens na lista utilizando o método extend. Diferentemente do método append, que adiciona 1 item por vez, o método extend() permite que adicionemos os itens de uma outra sequência no final da lista.
    itens.extend(("Joelho de Porco", "Alcatra", "Sobrecoxa de Frango"))

    # Agora, vamos gerar uma nova lista apenas com os itens Picanha, Costela e Maminha

    # Abaixo, apenas do limite final ser 4, pegamos apenas os itens que queremos. Chamamos esse índice final de exclusivo, pois ele não irá considerar o valor do limite final
    novos_itens = itens[1:4]
    print(novos_itens)

    # Se quisermos, podemos utilizar outro parâmetro (step), que indica de quantos em quantos itens queremos pegar
    print(itens[::2])

    # Se quisermos podemos utilizar índices negativos
    print(itens[:-3])

    # Invertendo os itens da lista
    print(itens[::-1])

    # ################################################################

    # Existe uma maneira mais "enxuta" de criar listas, chamada de list-comprehension. Geralmente criamos uma lista e adicionamos os itens dessa lista em um laço for, porém com list-comprehension podemos ter o mesmo comportamento de uma maneira mais direta.

    # Exemplo: Criar uma lista de números pares, do 1 até 100

    # Maneira "comum"
    lista_numeros = []

    # A função range gera um número a cada iteração do for
    for numero in range(1, 101):

        # Caso o resto da divisão seja 0, adiciona o número na lista
        if numero % 2 == 0:
            lista_numeros.append(numero)

    print(lista_numeros)

    # Criando a mesma lista com list-comprehension
    print([numero for numero in lista_numeros if numero % 2 == 0])

    # Cópia de listas em Python

    nome = "Amanda"
    nome2 = nome

    print(nome, nome2)

    ultimos_itens = itens
    print(itens, ultimos_itens)

    # Remove o item a partir do seu índice
    ultimos_itens.pop(4)

    # Remove o item a partir do valor
    ultimos_itens.remove("Joelho de Porco")

    # O método insert insere um novo item no índice especificado
    ultimos_itens.insert(0, "Bife Ancho")

    # Nesse caso, as alterações feitas na lista ultimos_itens irão se refletir na lista itens, pois na verdade as listas nada mais são que variáveis que estão apontando para a mesma posição de memória, onde estão armazenados os itens.

    print('-'*50)
    print(ultimos_itens)
    print(itens)

    itens.reverse()

    print('-'*50)
    print(ultimos_itens)
    print(itens)

    # Para resolver isso, podemos utilizar 2 abordagens:

    # Utilização do método copy()
    ultimos_itens2 = ultimos_itens.copy()
    ultimos_itens2.remove("Picanha")

    print('-'*50)
    print(ultimos_itens)
    print(ultimos_itens2)

    # Utilização de slice
    ultimos_itens3 = ultimos_itens[::]
    # Limpamos a lista
    ultimos_itens3.clear()

    print('-'*50)
    print(ultimos_itens)
    print(ultimos_itens3)