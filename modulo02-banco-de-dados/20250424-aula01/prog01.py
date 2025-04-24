"""
Python com banco de dados

Assim como em outras linguagens, podemos utilizar o python para acessar bancos de dados. Geralmente iremos precisar de uma biblioteca (conector) para acessar esses bancos. No caso do SQLite3, o python já vem por padrão com um conector para acessar esse tipo de banco de dados.

Bancos de dados SQLite são caracterizados por serem apenas 1 arquivo na máquina. São bastante utilizados em aplicações mobile, onde as vezes é necessário manter um banco de dados local no aparelho.

Trabalhando com SQLite
"""

import os

# 1) Importar a biblioteca
import sqlite3

if __name__ == "__main__":
    """
    Geralmente, seguimos os seguintes passos para trabalhar com banco de dados dentro de uma aplicação:
    1. Importamos a biblioteca (conector) de acesso ao banco de dados;
    2. Definimos uma connection string, que nada mais é do que uma string que contém as informações necessários para estabelecermos uma conexão com o banco de dados, como usuário, senha, endereço do servidor, etc;
    3. A partir dessa connection string, criamos a conexão com o banco de dados;
    4. A partir da conexão, criamos um cursor, que é o objeto que será utilizado para executar os comandos SQL no banco de dados;
    5. Definimos os comandos SQL como strings, e passamos para o cursor executá-los;
    6. Se necessário, pegamos o resultado do comando sql que foi executado.
    7. Fechamos a conexão com o banco de dados
    """

    # 2) Definir a connection string. No caso do SQLite, a connection string é simplesmente o caminho até o arquivo.
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    # 3) Criar a conexão com o banco de dados
    connection = sqlite3.connect(database=connection_string)

    # 4) Criar o cursor
    cursor = connection.cursor()

    # 5) Definindo os comandos que iremos executar
    # Vamos primeiramente criar a tabela tb_clientes

    # Primeiro vamos dar um DROP na tabela (se ela existir)
    sql = "DROP TABLE IF EXISTS tb_clientes;"
    cursor.execute(sql)

    # Agora vamos recriar a tabela
    sql = """
        CREATE TABLE tb_clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_de_nascimento TEXT,
            cidade TEXT NOT NULL
        );"""
    
    cursor.execute(sql)

    # 7) Fechamos a conexão com o banco de dados
    cursor.close()
    connection.close()