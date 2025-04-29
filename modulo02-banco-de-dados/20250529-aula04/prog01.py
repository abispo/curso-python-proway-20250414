"""
Programação Orientada a Objetos em Python

Classes, objetos, atributos e métodos
"""

# snake_case
# camelCase
# PascalCase
# UMA_CONSTANTE

# Para criação de classes em Python, utilizamos a palavra reservada class, seguido do nome da classe. De preferência, utilizamos o PascalCase na definição do nome. Mais detalhes, veja a pep8
class Pokemon:
    
    # O método __init__ é um método especial das classes em Python que serve para inicializar os atributos do objeto. O primeiro parâmetro de um método em Python, sempre será o self (com exceção de classmethods e staticmethods). O self é uma referência do próprio objeto que foi instanciado (semelhante ao this do Java).
    def __init__(self, name: str, type: str, health: int):

        # Abaixo, estamos criando 3 atributos: _name, _type e _health, e estamos atribuindo os valores recebidos no método inicializador. No Python, não temos nenhum mecanismo que defina o nível de acesso que qualquer coisa que seja (classe, atributo, método, etc), então seguimos a padronização de, caso o nome do atributo/método comece com underline(_), deve ser considerado privado
        self._name = name
        self._type = type
        self._health = health

        def attack(self):
            print(f"{self._name} attacks!")
        