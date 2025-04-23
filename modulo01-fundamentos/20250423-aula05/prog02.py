
from requests.exceptions import ConnectionError

import requests

access_token = ""
BASE_URL = "https://superheroapi.com/api/{}".format(access_token)

if __name__ == "__main__":

    try:
        r = requests.get(
            "{}/{}".format(BASE_URL, 423)
        )

        print(r.json())

    except Exception as exc_info:
        print("Aconteceu um erro: {}".format(str(exc_info)))

    else:
        print("Requisição realizada com sucesso!")

    finally:
        print("Fechando conexão...")
