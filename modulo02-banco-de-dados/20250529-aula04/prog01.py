"""
Programação Orientada a Objetos em Python

Classes, objetos, atributos e métodos
"""

# snake_case
# camelCase
# PascalCase
# UMA_CONSTANTE

from pokemons import Pokemon

if __name__ == "__main__":
    
    # Abaixo, instanciamos a classe pokemon, e salvamos esse objeto na variável pikachu.
    pikachu = Pokemon(
        name="Pikachu",
        type="Elétrico",
        health=40
    )

    # Abaixo, estamos chamando o método get_name()
    print(f"Pokemon '{pikachu.get_name()}' criado!")

    # Chamando os atributos definidos com property
    # O decorator @property faz com que os métodos sejam chamados como atributos do objeto.
    pikachu.type = "Trovão"
    pikachu.health = 50

    print(pikachu.health)
