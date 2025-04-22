"""
Entrada e saída de arquivos em Python (File I/O)

Lendo arquivos .txt em Python
"""

if __name__ == "__main__":
    
    """
    Para abrir arquivos em Python, utilizamos a função built-in open(). Podemos abrir quaisquer tipos de arquivos em Python, tanto arquivos texto quanto binários. A função open possui apenas 1 parâmetro obrigatório, que é o caminho/nome do arquivo a ser aberto
    """

    arquivo = open(file="linguagens.txt", mode="r")