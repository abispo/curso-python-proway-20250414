"""
Python com banco de dados

Trabalhando com MySql utilizando a biblioteca PyMysql
"""

import json
import os
import shutil

from dotenv import load_dotenv

import pymysql.cursors
import requests

# A função load_dotenv() vai carregar o arquivo .env, e transformar as constantes em variáveis de ambiente. Caso queiramos mudar o nome do arquivo, temos que informar como parâmetro dessa função.
load_dotenv()

if __name__ == "__main__":

    # Criando a conexão informando direto a connection string
    connection = pymysql.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        port=int(os.getenv("PORT")),
        cursorclass=pymysql.cursors.DictCursor
    )
    
    # Criação do cursor
    cursor = connection.cursor()

    sql = "DROP TABLE IF EXISTS tb_opcoes;"
    cursor.execute(sql)

    sql = "DROP TABLE IF EXISTS tb_perguntas;"
    cursor.execute(sql)

    # Criação da tabela de perguntas
    sql = """
        CREATE TABLE tb_perguntas(
            id INT PRIMARY KEY AUTO_INCREMENT,
            texto VARCHAR(200) NOT NULL
        );"""
    cursor.execute(sql)

    # Criação da tabela de opções
    sql = """
        CREATE TABLE tb_opcoes(
            id INT PRIMARY KEY AUTO_INCREMENT,
            pergunta_id INT NOT NULL,
            texto VARCHAR(100) NOT NULL,
            votos INT NOT NULL DEFAULT 0,
            FOREIGN KEY(pergunta_id)
            REFERENCES tb_perguntas(id)
        );"""
    cursor.execute(sql)

    # Agora vamos baixar o arquivo com as perguntas e opções, e posteriormente salvar nas tabelas correspondentes.
    url = "https://raw.githubusercontent.com/abispo/shared-files/refs/heads/main/enquetes.json"
    r = requests.get(url)

    tmp_dir = os.path.join(os.getcwd(), "tmp")
    file_dir = os.path.join(tmp_dir, "enquetes.json")

    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)

    with open(file_dir, mode="w+", encoding="utf-8") as json_file:
        json_file.write(r.text)

        # Precisamos jogar a posição do cursor no início do arquivo, para conseguirmos ler o seu conteúdo
        json_file.seek(0)

        # Transformamos o conteúdo lido no arquivo em um objeto Python (nesse caso, um dicionário)
        questions = json.loads(json_file.read())

        for question in questions:
            question_text = question.get("pergunta")
            sql = "INSERT INTO tb_perguntas(texto) VALUES (%s)"

            # A string especial %s será substituída pelo valor da variável question_text
            cursor.execute(sql, question_text)

            # Se utilizarmos os comandos INSERT, UPDATE ou DELETE, precisamos "confirmar" a transação utilizando o método commit(). Enquanto o commit não for chamado, os comandos ficam "enfileirados".
            connection.commit()

            # O atributo lastrowid do cursor armazena o valor da chave primária do último registro salvo
            question_id = cursor.lastrowid
            choices = question.get("opcoes")

            for choice in choices:
                text = choice.get("texto")
                votes = choice.get("votos", 0)
                sql ="""
                    INSERT INTO tb_opcoes(pergunta_id, texto, votos) VALUES (
                        %s, %s, %s
                    )"""

                cursor.execute(
                    query=sql,
                    args=(question_id, text, votes),
                )
                connection.commit()

    # Para consultar os dados nas tabelas, podemos utilizar 3 métodos:

    # fetchone() -> Retorna apenas 1 registro da consulta. Caso a consulta não retorne dados, o método retorna None
    sql = "SELECT * FROM tb_perguntas;"
    cursor.execute(sql)

    print("{}".format(cursor.fetchone()))

    # fetchmany(size) -> Retorna a quantidade de registros indicados no parâmetro size. Caso a consulta não retorne nada ou o cursor já esteja no final do resultado, será retornada uma lista vazia
    print("{}".format(cursor.fetchmany(10)))

    # fetchall() -> Retorna todos os registros restantes da consulta. Caso não existam mais registros a serem exibidos, retorna uma lista vazia
    print("{}".format(cursor.fetchall()))

    # Como o cursor chegou no final do resultado, não há mais registros a serem exibidos.
    print("{}".format(cursor.fetchall()))

    # Fechando a conexão e excluindo o arquivo temporário
    cursor.close()
    connection.close()

    # Remoção do diretório temporário
    shutil.rmtree(tmp_dir)
