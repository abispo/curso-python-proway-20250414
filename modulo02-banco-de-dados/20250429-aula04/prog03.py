"""
Programação Orientada a Objetos em Python

Composição
----------

Composição ocorre quando uma classe compõe ou é composta por uma ou mais classes
"""

from random import shuffle

# A classe object é a classe fundamental do Python, de onde todas as classes são herdadas. A herança para essa classe é feita de maneira implícita, mas podemos herdar explicitamente, como na classe Carta. 
class Carta(object):

    def __init__(self, naipe: str, valor: str):
        self._naipe = naipe
        self._valor = valor

    # O método mágico __str__ é utilizado pelo print para exibir uma representação desse objeto de maneira inteligível para o ser humano. Caso não criarmos esse método na classe, ele será herdado de objeto, e terá um comportamento padrão
    def __str__(self):
        return f"{self._valor}{self._naipe}"
    
    # o __repr__ é semelhante ao __str__, porém é utilizado quando o objeto estiver dentro de um container (lista, tupla, etc)
    def __repr__(self):
        return f"{self._valor}{self._naipe}"

class Baralho:

    def __init__(self):
        
        # Atributo que irá armazenar a lista de objetos Carta
        self._cartas = []

        # Lista de naipes que será utilizada na "montagem" do baralho 
        self._naipes = [
            "\u2660", "\u2665", "\u2663", "\u2666"
        ]

        # Lista de valores que será utilizada na "montagem" do baralho
        self._valores = [
            "2", "3", "4", "5", "6", "7", "8",
            "9", "10", "J", "Q", "K", "A"
        ]

        # Aqui utilizamos um for encadeado para montar o baralho. Para cada naipe, serão geradas as cartas com o naipe e os valores
        for naipe in self._naipes:
            for valor in self._valores:
                self._cartas.append(Carta(naipe, valor))

        # Por fim, utilizamos a função shuffle para embaralhar esse baralho
        shuffle(self._cartas)

    # Aqui utilizamos o método __str__ para o mesmo fim da Carta
    def __str__(self):
        return str(self._cartas)
        # return " | ".join([str(carta) for carta in self._cartas])

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self._cartas):
            carta = self._cartas[self._index]
            self._index += 1

            return carta
        
        else:
            raise StopIteration()

if __name__ == "__main__":
    baralho = Baralho()

    print(baralho)
    
    for carta in baralho:
        print(carta, end=" ")
