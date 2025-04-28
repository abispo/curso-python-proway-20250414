-- Criar banco de dados da aula
CREATE DATABASE IF NOT EXISTS modulo02_python_formasnormais;
USE modulo02_python_formasnormais;

-- Execute o comando abaixo se quiser apagar o banco de dados
DROP DATABASE IF EXISTS modulo02_python_formasnormais;

/*
Segunda Forma Normal (2FN)

Para uma tabela estar na 2FN, ela precisa necessáriamente:
* Estar na 1FN
* Não devem existir dependências parciais. Ou seja, todas as colunas não chave da tabela devem depender
* exclusivamente de todas as partes da chave primária. Chamamos isso de dependência funcional total.
*/

-- Criação da tabela tb_cursos
CREATE TABLE IF NOT EXISTS tb_cursos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	carga_horaria INT NOT NULL
);
INSERT INTO tb_cursos(nome, carga_horaria) VALUES
	("Fundamentos de Python", 20),
	("Java Avançado", 50),
	("Linux básico", 35);
SELECT * FROM tb_cursos;

-- Criação da tabela de cursos e instrutores
CREATE TABLE IF NOT EXISTS tb_cursos_instrutores(
	curso_id INT NOT NULL,
	instrutor_id INT NOT NULL,
	nome_instrutor VARCHAR(100) NOT NULL,
	email_instrutor VARCHAR(100) NOT NULL,
	PRIMARY KEY(curso_id, instrutor_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id)
);
DESCRIBE tb_cursos_instrutores;

-- Inserir dados de cursos e instrutores
INSERT INTO tb_cursos_instrutores(curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
	(1, 1, "Guido von Rossum", "guido@email.com"),
	(2, 2, "João da Silva", "joao@email.com"),
	(3, 3, "Linus Torvalds", "linus@email.com");
SELECT * FROM tb_cursos_instrutores;

INSERT INTO tb_cursos(nome, carga_horaria) VALUES
	("Formação PHP", 80);

INSERT INTO tb_cursos_instrutores(curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
	(4, 2, "Rasmus Lerdorf", "joao@email.com");

SELECT a.id, a.nome, b.instrutor_id, b.nome_instrutor, b.email_instrutor FROM tb_cursos a
INNER JOIN tb_cursos_instrutores b
ON a.id = b.curso_id;

-- Acima, temos um problema com relação ao instrutor 2. Temos informações divergentes de nome e e-mail. Para resolver esse problema
-- vamos criar a tabela tb_instrutores, onde vamos segregar essas informações.
-- Primeiro, removemos as colunas que dependem parcialmente da chave primária
ALTER TABLE tb_cursos_instrutores DROP COLUMN nome_instrutor;
ALTER TABLE tb_cursos_instrutores DROP COLUMN email_instrutor;

-- Criar a tabela de instrutores
CREATE TABLE IF NOT EXISTS tb_instrutores(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL
);

INSERT INTO tb_instrutores (nome, email) VALUES
	("Guido von Rossum", "guido@email.com"),
	("João da Silva", "joao@email.com"),
	("Linus Torvalds", "linus@email.com"),
	("Rasmus Lerdorf", "rasmus@email.com");
	
-- Agora, vamos criar a referência para instrutores na tabela tb_cursos_instrutores
ALTER TABLE tb_cursos_instrutores ADD FOREIGN KEY (instrutor_id) REFERENCES tb_instrutores(id);

SELECT a.nome, c.id, c.nome, c.email FROM tb_cursos a
INNER JOIN tb_cursos_instrutores b
ON a.id = b.curso_id
INNER JOIN tb_instrutores c
ON b.instrutor_id = c.id;