"""
Trabalhando com arquivos .csv no Python

CSV -> Comma Separated Values | Valores Separados por vírgula

Escrevendo em arquivos .csv com csv.writer e csv.DictWriter
"""

import csv
import os

if __name__ == "__main__":

    # Também podemos utilizar o poder do pacote csv para escrever em arquivos, e os objetos trabalham de maneira semelhante aos métodos csv.reader e csv.DictReader()

    lista_compras = [
        ["Maria", 567.43, 215.89, 339.65],
        ["Cláudia", 34.77, 127.55, 78.12],
        ["Elizabeth", 11.90, 354.66, 155.01]
    ]
    # Dados que serão salvos no arquivo

    root_dir = os.getcwd()
    file_dir = os.path.join(root_dir, "compras_clientes.csv")

    with open(file_dir, mode="w", encoding="utf-8", newline="") as arquivo:
        # Precisamos do parâmetro newline="", pois senão será salvo uma quebra de linha a mais quando chamarmos os métodos writerow e writerows
        
        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # Salva uma linha no arquivo. Essa linha deve ser uma lista dos valores
        arquivo_csv.writerow(["nome", "compra_1", "compra_2", "compra_3"])

        # Salva várias linhas de uma vez no arquivo. É necessário passar uma lista de listas
        arquivo_csv.writerows(lista_compras)

    with open(os.path.join(root_dir, "acessos.csv"), mode="w", encoding="utf-8", newline="") as arquivo:
        lista_acessos = [
            {"nome": "José", "ultimo_acesso": "20250422"},
            {"nome": "Paulo", "ultimo_acesso": "20250421"},
            {"nome": "Mariano", "ultimo_acesso": "20250328"},
        ]

        arquivo_csv = csv.DictWriter(
            arquivo,
            fieldnames=["nome", "ultimo_acesso"],
            delimiter=';'
        )

        # Salvando apenas a linha com o cabeçalho do arquivo
        arquivo_csv.writeheader()

        # Salvando apenas 1 linha no arquivo
        arquivo_csv.writerow({"nome": "Daniel", "ultimo_acesso": "20250405"})

        # Salvando várias linhas de uma vez só
        arquivo_csv.writerows(lista_acessos)