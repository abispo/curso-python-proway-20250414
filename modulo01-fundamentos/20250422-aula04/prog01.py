"""
Entrada e saída de arquivos em Python (File I/O)

Lendo arquivos .txt em Python
"""

if __name__ == "__main__":
    
    """
    Para abrir arquivos em Python, utilizamos a função built-in open(). Podemos abrir quaisquer tipos de arquivos em Python, tanto arquivos texto quanto binários. A função open possui apenas 1 parâmetro obrigatório, que é o caminho/nome do arquivo a ser aberto
    """

    arquivo = open(file="linguagens.txt", mode="r")

    """
    Como mencionado acima, o parâmetro file é obrigatório. Aqui indicamos o caminho/nome do arquivo. Caso o arquivo esteja no mesmo diretório que o script python que está sendo executado, basta passar apenas o nome do arquivo.

    O parâmetro mode, apesar de ser opcional, é muito importante. Aqui definimos o modo de abertura do arquivo. Caso não informemos o valor, por padrão ele recebe 'r' (read only/somente leitura)

    Abaixo estão os modos possíveis de se abrir um arquivo. Não há problema em mesclá-los:

    r   -> Read Only/Modo somente leitura. Não conseguimos fazer modificações no arquivo, apenas ler o seu conteúdo.
    w   -> Write Only/Somente escrita. Nesse modo, caso o arquivo não exista, ele será criado. E caso ele exista, o seu conteúdo é sobreposto (truncado) com o nome conteúdo inserido.
    a   -> Append/Adicionar ao final. Caso o arquivo não exista, ele será criado. E caso exista, todo novo conteúdo inserido será colocado a partir do final do arquivo.
    """