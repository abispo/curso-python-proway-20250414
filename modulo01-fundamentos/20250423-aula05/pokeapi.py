
import os
import requests

from messages import pokemon_info

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

if __name__ == "__main__":

    pokemon_name = input("Informe o nome de um Pokémon: ")

    r = requests.get(
        "{}/{}".format(BASE_URL, pokemon_name)
    )

    if r.status_code != 200:
        print(f"Não foi possível carregar informações do pokémon '{pokemon_name}'")

    else:
        body = r.json()

        abilities_list = []

        for habilit_info in body["abilities"]:
            abilities_list.append(habilit_info["ability"]["name"])

        base_experience = body["base_experience"]
        ID = body["id"]
        name = body["name"]
        height = body["height"]
        weight = body["weight"]

        types_list = []

        for type_info in body["types"]:
            types_list.append(type_info["type"]["name"])

        output = pokemon_info.format(
            ", ".join(abilities_list),
            base_experience,
            ID,
            name,
            height,
            weight,
            ", ".join(types_list)
        )

        print('*'*20)
        print(output)

        base_dir = os.getcwd()
        pokemons_dir = os.path.join(base_dir, "pokemons")

        if not os.path.exists(pokemons_dir):
            os.mkdir(pokemons_dir)

        with open(os.path.join(pokemons_dir, f"{pokemon_name}.txt"), mode="w", encoding="utf-8") as arquivo:
            arquivo.write(output)
        