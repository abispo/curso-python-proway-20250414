"""
Entrada e saída de arquivos em Python (File I/O)

Escrevendo arquivos .txt em Python
"""

import os

if __name__ == "__main__":

    """
    Assim como a leitura, a escrita de arquivo em Python é bem simples, apenas precisamos tomar cuidado com alguns detalhes.
    """

    root_dir = os.getcwd()
    # A função getcwd() retorna o caminho completo até o diretório raiz da aplicação

    temp_dir = os.path.join(root_dir, "temp")
    # O método os.path.join mescla vários caminhos em um só. No caso acima, estamos concatenando o caminho para o diretório raiz da aplicação com o nome da pasta que vamos criar

    if not os.path.exists(temp_dir):
        # A função os.path.exists verifica se um caminho existe. Esse caminho pode ser tanto o nome de uma pasta quanto o nome de um arquivo.

        os.mkdir(temp_dir)
        # A função mkdir cria um novo diretório no sistema de arquivos.

    # Aqui abrimos o arquivo lista.txt no modo somente escrita
    with open(os.path.join(temp_dir, "lista.txt"), mode="w") as arquivo:
        print("O arquivo {}".format("está fechado" if arquivo.closed else "está aberto."))
        arquivo.write("Banana\n")
        arquivo.write("Abacate\n")
        
        itens = ["Tomate\n", "Alface\n", "Fruta", " do ", "conde\n"]
        arquivo.writelines(itens)

    print("O arquivo {}".format("está fechado" if arquivo.closed else "está aberto."))
    
    # Por fim, abrimos novamente o arquivo, porém no modo "append", onde o conteúdo será adicionado a partir do final do arquivo
    with open(os.path.join(temp_dir, "lista.txt"), mode="a", encoding="utf-8") as arquivo:
        arquivo.write("Abacaxi\n")
        arquivo.writelines(["Manga\n", "Limão\n", "Maçã"])