# Utilizamos o caractere '#' quando queremos criar um comentário. Comentários são ignorados pelo interpretador.

# Por boas práticas, caso o nosso script seja executado diretamente pelo interpretador, colocamos a expressão abaixo.
# Uma expressão em Python é um conjunto de instruções que retornam um valor. No caso abaixo, o valor retornado é do tipo bool (booleano)
# Sempre que utilizamos laços de condição e de repetição, estamos criando um novo bloco de código. No Python, sempre que criarmos um novo bloco, é obrigatório seguir as regras de identação da linguagem. Por padrão, cada novo bloco de código tem um espaçamento de 4 espaços.
if __name__ == "__main__":

    # Abaixo estamos utilizando as funções de entrada e saída (I/O) via terminal do Python.

    # A função input espera o usuário entrar com alguma informação pelo terminal. Ela recebe um parâmetro, que é o texto a ser exibido no terminal
    nome = input("Informe o seu nome: ")

    # A função print recebe um parâmetro que será impresso no terminal.
    print("Olá " + nome + ". Bem-vindo ao curso de Python.")
