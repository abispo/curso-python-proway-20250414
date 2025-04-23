"""
Trabalhando com arquivos .csv no Python

CSV -> Comma Separated Values | Valores Separados por vírgula

Lendo o conteúdo de arquivos com csv.reader e csv.DictReader
"""

import csv
from datetime import datetime
import os

def mostra_info(codigo: str, nome: str, data_nascimento: str, genero: str):
    data_nasc = datetime.strptime(data_nascimento, "%Y%m%d")
    # O método strptime do objeto datetime converte uma string no formato de data em um objeto datetime
    idade = (datetime.now() - data_nasc).days / 365
    # A subtração do resultado do método now() pela nova data criada, irá retornar um objeto timedelta, que é o resultado de uma operação entre 2 datas. Estamos pegando a diferença de dias entre essas 2 datas e dividindo por 365, que resultará na diferença de anos.

    saida = """
    Código: {}
    Nome: {}
    Idade: {:.1f}
    Gênero: {}""".format(
        codigo,
        nome,
        idade,
        "Masculino" if genero.lower() == 'm' else "Feminino"
    )

    print(saida)

if __name__ == "__main__":

    """
    Apesar de ser um arquivo texto comum, o python possui um pacote próprio para se trabalhar com arquivos .csv, que é o pacote csv. Com esse pacote a manipulação desse arquivo fica mais fácil.
    """

    root_dir = os.getcwd()
    file_dir = os.path.join(root_dir, "clientes.csv")

    with open(file_dir, mode="r", encoding="utf-8") as arquivo:

        arquivo_csv = csv.reader(arquivo, delimiter=';')
        # O método csv.reader retorna um objeto do tipo arquivo csv. Ele é criado a partir do objeto arquivo que é retornado pela função built-in open()
        # Como o caractere separador do nosso arquivo .csv é um ponto-e-vírgula, precisamos informar no parâmetro delimiter. Se não fizermos isso, a leitura do arquivo não será da maneira correta.

        for linha in arquivo_csv:
            print(linha)


    with open(file_dir, mode="r", encoding="utf-8") as arquivo:
        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            mostra_info(**linha)