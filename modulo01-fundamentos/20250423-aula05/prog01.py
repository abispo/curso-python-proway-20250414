
import requests

URL_BASE = "https://parallelum.com.br/fipe/api/v1/carros"
URL_MARCAS = f"{URL_BASE}/marcas"
URL_MODELOS = "{}/{}/modelos"

if __name__ == "__main__":

    while True:
        
        print("Escolha uma marca: ")
        marcas = requests.get(URL_MARCAS).json()

        for marca in marcas:
            print("{}) {}".format(*marca.values()))

        print('-'*20)
        codigo_marca = int(input("Informe o código da marca (0 para sair): "))

        if codigo_marca == 0:
            break

        modelos = requests.get(
            URL_MODELOS.format(URL_MARCAS, codigo_marca)
        ).json()

        lista_models = modelos["modelos"]

        for modelo in lista_models:
            print("{}) {}".format(*modelo.values()))

        print('-'*20)
        codigo_modelo = int(input("Informe o código do modelo (0 para sair): "))

        if codigo_modelo == 0:
            break