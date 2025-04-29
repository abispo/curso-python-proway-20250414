-- Criar banco de dados da aula
CREATE DATABASE IF NOT EXISTS modulo02_python_formasnormais;
USE modulo02_python_formasnormais;

-- Execute o comando abaixo se quiser apagar o banco de dados
DROP DATABASE IF EXISTS modulo02_python_formasnormais;

/*
Terceira Forma Normal (3FN)

Uma tabela está na 3F, se:
* Está na 2FN
* Todas as colunas não chave da tabela dependem exclusivamente da chave primária, e não de outras colunas não chave. Chamamos essa
* dependendência de dependência transitiva
*/

CREATE TABLE IF NOT EXISTS tb_itens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL
);

INSERT INTO tb_itens(nome, valor_unitario) VALUES
	("Conjunto de dados para RPG", 25),
	("O Senhor dos Anéis: A Sociedade do Anel", 39.90),
	("Eldritch Horror Board Game", 399.90),
	("Jogo de Xadrez", 29.90),
	("Conjunto de cartas de Magic", 49.90);
SELECT * FROM tb_itens;

CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora DATETIME DEFAULT NOW(),
	descricao VARCHAR(500)
);
DESCRIBE tb_pedidos;
	
INSERT INTO tb_pedidos(descricao) VALUES
	("Pedido compacto"),
	("Primeiro pedido na loja"),
	("Presente"),
	("Troca de itens");

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	item_id INT NOT NULL,
	pedido_id INT NOT NULL,
	quantidade INT NOT NULL,
	subtotal FLOAT NOT NULL,
	PRIMARY KEY(item_id, pedido_id),
	FOREIGN KEY(item_id) REFERENCES tb_itens(id),
	FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id)
);
DESCRIBE tb_pedidos_itens;

INSERT INTO tb_pedidos_itens(item_id, pedido_id, quantidade, subtotal) VALUES
	(1, 1, 3, 25 * 3),
	(3, 1, 1, 399.90),
	(4, 2, 5, 29.90 * 5),
	(1, 3, 3, 19.90 * 3);
	
SELECT * FROM tb_pedidos_itens;

SELECT format() 

ALTER TABLE tb_pedidos_itens DROP COLUMN subtotal;

SELECT c.id AS "pedido_id", a.nome, a.valor_unitario, b.quantidade, FORMAT(a.valor_unitario * b.quantidade, 2) AS "subtotal" FROM tb_itens a
INNER JOIN tb_pedidos_itens b
ON a.id = b.item_id
INNER JOIN tb_pedidos c
ON b.pedido_id = c.id
ORDER BY pedido_id;