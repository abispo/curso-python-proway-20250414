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
    r+  -> Indicamos que estamos abrindo o arquivo para leitura e escrita ao mesmo tempo

    E além disso, podemos indicar também o tipo de arquivo que estamos abrindo: arquivo somente texto(t) e arquivo binário (b). Por padrão, se não informarmos, a função open() irá assumir que um arquivo texto está sendo aberto. Para indicarmos o tipo de arquivo, passamos junto com o modo. Exemplo:

    open("notas.txt", rt)       # Estamos abrindo o arquivo notas.txt, indicando que é um arquivo texto que será aberto no modo somente leitura
    open("virus.exe", ab)       # Estamos abrindo o arquivo virus.exe, indicando que é um arquivo binário e que será aberto no modo append.
    """

    """
    Podemos abrir um arquivo Python de maneiras diferentes. Quando abrimos no modo somente leitura, temos acesso aos seguintes métodos
    """
    print(arquivo.read(10))
    # O método read() lê o conteúdo do arquivo e retorna como uma string. Caso não informemos o primeiro parâmetro, esse método irá ler o arquivo inteiro.

    print(arquivo.readline(20))
    # O método readline lê uma linha por vez, até chegar no caractere oculto newline. Não importa o valor que passemos para o parâmetro size, o método lerá apenas até o final da linha. Caso não passemos nada, ele lê a linha inteira.
    
    print(arquivo.readline())
    # Agora na linha acima, todo o conteúdo da próxima linha será lido, até chegar no caractere nova linha, não importando quantos caracteres existam nessa linha.

    print(arquivo.readlines(11))
    # O método readlines() lê o conteúdo do arquivo e retorna uma lista de strings, com cada string representando uma linha do arquivo. Caso o cursor pare antes do final da linha, o método readlines() pega a linha toda do mesmo jeito.

    print('*'*20)

    print(arquivo.readlines())
    # Como o cursor está no final do arquivo, qualquer chamada para ler o conteúdo, vai resultar no retorno de uma string ou de uma lista vazia

    print("Posição do cursor: {}".format(arquivo.tell()))
    # O método tell() indica a posição atual do cursor.
    # Caso queiramos retornar ao início do arquivo, utilizamos o método seek()

    arquivo.seek(0)
    # Acima, estamos reposicionando o cursor na posição 0 do arquivo. Assim, podemos lê-lo novamente

    print(arquivo.readlines())
    # Mostramos novamente todo o conteúdo do arquivo

    print("Estado do arquivo: {}".format(arquivo.closed))

    arquivo.close()
    # É muito importante sempre fecharmos os arquivos que abrimos. No módulo de escrita de arquivo, vamos ver uma maneira de fechar o arquivo automaticamente

    print("Estado do arquivo: {}".format(arquivo.closed))