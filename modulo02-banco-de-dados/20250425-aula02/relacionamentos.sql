/*
Aula 02 - Relacionamentos entre tabelas no banco de dados

Um dos principais conceitos que definem um banco de dados relacional, são as
relações entre as tabelas desse banco. Existem 3 níveis de relacionamento que
podem existir entre tabelas:

Um-para-um: 1:1
Um-para-muitos: 1:N
Muitos-para-Muitos: N:N

Entender como as tabelas se relacionam é um passo fundamental na parte de modelagem
dos dados da nossa aplicação. Relacionamentos mal definidos levam a perda de
consistência e confiabilidade dos dados.

Para ilustrar esses tipos de relaciomantos, vamos montrar uma estrutura de tabelas
que irá armazenar os dados de um sistema fictício de postagens (blog). Para modelar
essas tabelas, precisamos entender as regras desse negócio, que são as seguintes:

No sistema, haverão as seguintes entidades: Usuario, Perfil, Postagem,
Comentário e Categoria.

Um usuário do sistema, deverá ter as seguintes informações armazenadas
* Nome
* Sobrenome
* Data de nascimento
* Email
* Senha

No caso acima, vamos salvar em tabelas separadas os dados de acesso e os dados de perfil
de cada usuário. Os dados de acesso serão email e senha, e os dados de perfil serão nome,
sobrenome e data de nascimento.

Ou seja, para cada registro na tabela de usuarios, deve existir 1 e apenas 1 registro
na tabela de perfis. Pra essa relação, teremos um relacionamento 1:1
*/

-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS tb_usuarios(
	# Uma chave primária é definida como uma coluna que não terá valores repetidos
	# No caso abaixo, a coluna id é do tipo numérico (inteiro), chave primária e auto incremento
	# ou seja, o valor do id vai se auto incrementar quando houver um INSERT nessa tabela.
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	senha VARCHAR(200) NOT NULL
);

-- Criação da tabela de perfis
CREATE TABLE IF NOT EXISTS tb_perfis(
	id INT PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	sobrenome VARCHAR(100) NOT NULL,
	data_de_nascimento DATETIME NULL,
	FOREIGN KEY (id) REFERENCES tb_usuarios(id)
);

-- Acima criamos a tabela tb_perfis. A coluna id é, ao mesmo tempo, chave primária e chave estrangeira
-- da tabela, referenciando a coluna id da tabela tb_usuarios. Ou seja, o id inserido obrigatoriamente
-- deve existir na tabela tb_usuarios, e ao mesmo tempo não deve se repetir na tabela de perfis

INSERT INTO tb_usuarios (email, senha) VALUES ("maria@email.com", "maria123");
INSERT INTO tb_usuarios (email, senha) VALUES ("jose@email.com", "jose123");
INSERT INTO tb_usuarios (email, senha) VALUES ("joao@email.com", "joao123");

SELECT * FROM tb_usuarios tu ;

-- Inserir dados na tabela de perfis
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
	(1, "Maria", "das Dores", NULL);
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
	(2, "José", "da Silva", "1977-05-19");
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
	(3, "João", "Carvalho", "1980-03-07");
SELECT * FROM tb_perfis tp;

-- O comando abaixo falhará, pois já existe um id existente na tabela
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
	(3, "Barbara", "Cardoso", NULL);

-- O comando abaixo falhará, pois tenta inserir um id que não existe na tabela de usuários,
-- resultando em erro
INSERT INTO tb_perfis (id, nome, sobrenome, data_de_nascimento) VALUES
	(10000, "Denis", "Orlando", NULL);


