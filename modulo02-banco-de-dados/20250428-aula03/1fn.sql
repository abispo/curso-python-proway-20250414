-- Criar banco de dados da aula
CREATE DATABASE IF NOT EXISTS modulo02_python_formasnormais;
USE modulo02_python_formasnormais;

-- Execute o comando abaixo se quiser apagar o banco de dados
DROP DATABASE IF EXISTS modulo02_python_formasnormais;

/*
Primeira Forma Normal (1FN)

Para uma tabela estar na 1FN, devemos nos assegurar que as
seguintes regras são válidas:
* Deve existir ao menos 1 coluna chave primária
* Os valores das colunas não devem ser compostos (devem ser indivisíveis)
* Não podem existir colunas multivaloradas
*/

-- Exemplo de tabela de viola a 1FN
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT NOT NULL,
	nome VARCHAR(100),
	endereco VARCHAR(200),
	telefone VARCHAR(50)
);

INSERT INTO tb_clientes (id, nome, endereco, telefone) VALUES
	(1, "João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "47912345678"),
	(2, "Maria das Graças", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "4798754321,4798765234"),
	(3, "José Carvalho", "Rua dos Bandeirantes, 240, Centro, Pomerode, SC", "47943211234");

SELECT * FROM tb_clientes;

-- A tb_clientes não está na 1FN, pois viola todas as regras:
-- * Não possui uma chave primária.
-- * A coluna endereco pode ser quebrada em outras colunas.
-- * No usuário de id 2, a coluna telefone possui mais de 1 valor.

INSERT INTO tb_clientes(id, nome, endereco, telefone) VALUES
	(2, "Bruna Fonseca", "Rua João Karsten, 200, Testo Salto, Blumenau, SC", "47912347890");
SELECT * FROM tb_clientes WHERE endereco LIKE "%SC%";

RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

-- Criação da tabela seguindo as regras da 1FN
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	tipo_logradouro VARCHAR(30) NOT NULL,
	nome_logradouro VARCHAR(100) NOT NULL,
	numero VARCHAR(10) NULL,
	bairro VARCHAR(100) NOT NULL,
	cidade VARCHAR(100) NOT NULL,
	estado CHAR(2) NOT NULL
);
ALTER TABLE tb_clientes RENAME COLUMN nome_logradouro TO logradouro;
ALTER TABLE tb_clientes ADD COLUMN nome VARCHAR(100) NOT NULL;
DESCRIBE tb_clientes;

INSERT INTO tb_clientes (nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado) VALUES
	("João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	("Maria das Graças", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
	("José Carvalho", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");
SELECT * FROM tb_clientes;
	

-- Acima resolvemos 2 problemas: Criamos a tabela com a chave primária, e quebramos a coluna
-- endereco em várias outras colunas
-- No caso da coluna telefone, como alguns usuarios podem ter mais de 1, é necessário criar
-- uma nova tabela
CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	FOREIGN KEY (cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_telefones (cliente_id, telefone) VALUES
	(1, "47912345678"),
	(2, "4798754321"),
	(2, "4798765234"),
	(3, "47943211234");
SELECT * FROM tb_telefones;

SELECT a.id, a.nome, b.telefone FROM tb_clientes a
INNER JOIN tb_telefones b
ON a.id = b.cliente_id;