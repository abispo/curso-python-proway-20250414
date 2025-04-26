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

/*
Continuando, vamos criar a a tabela de postagens, que irá armazenar as postagens feitas pelos
usuários. As regras para postam, são as seguintes:
* Um usuário pode ter 0, 1 ou mais postagens
* Uma postagem pode ter 1 e apenas 1 autor (usuario)
* Cada postagem deve ser salva com as seguintes informações:
* 	id da postagem
* 	id do autor dessa postagem (id do usuario)
* 	titulo da postagem
* 	texto da postagem
* 	data/hora de criação da postagem 
*/

CREATE TABLE IF NOT EXISTS tb_postagens(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	usuario_id INTEGER NOT NULL,
	titulo VARCHAR(200) NOT NULL,
	texto TEXT NOT NULL,
	# A linha abaixo indica que o valor padrão que será salvo na coluna data_hora, será a data e hora atuais, que são
	# retornadas pela função NOW()
	data_hora DATETIME DEFAULT NOW(),
	FOREIGN KEY(usuario_id) REFERENCES tb_usuarios(id)
);

-- Inserir postagens na tabela
INSERT INTO tb_postagens (usuario_id, titulo, texto) VALUES
	(1, "A linguagem Python", "Python é popular em machine learning e big data."),
	(1, "A linguagem Java", "Java é uma linguagem antiga, porém ainda muito utilizada."),
	(1, "A linguagem Cobol", "Cobol é utilizada majoritariamente em sistemas bancários."),
	(2, "A linguagem Javascript", "Javascript é uma das linguagens mais populares existentes.");
	
SELECT * FROM tb_postagens tp;

/*
Observamos que um usuário, pode ter nenhuma postagem (usuario_id 3), 1 postagem (usuario_id_2) e várias postagens(
usuario_id 3). Acima acabamos de criar um relacionamento do tipo Um-Para-Muitos. Ou seja, cada linha na tabela tb_usuarios
pode ter 0, 1 ou mais linhas correspondentes na tabela tb_postagens.
*/

-- Pegar todas as postagens feitas pelo usuario 1 (maria)
-- Estamos usuando apelidos para as tabelas: tb_usuarios é a, tb_postagens é b
SELECT a.id, b.titulo, b.texto, b.data_hora FROM tb_usuarios a
INNER JOIN tb_postagens b
ON a.id = b.usuario_id 
AND a.id = 1;

/*
Continuando, para cada postagem feita, podemos definir categorias para essa postagem. Por exemplo: a postagem
"A linguagem Python", pode fazer parte das categorias "programacao", "python", "ti". Assim como a categoria "ti" pode
aparecer em diversas postagens. Ou seja, podemos filtrar AS postagens de acordo com determinada categoria.

Nesse caso, vamos criar um relaciomamento que prevê esses cenários:
*/

-- Criar a tabela de categorias
CREATE TABLE IF NOT EXISTS tb_categorias(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL
);

INSERT INTO tb_categorias (nome) VALUES
	("programacao"),
	("python"),
	("banco-de-dados"),
	("mysql"),
	("java"),
	("linux"),
	("devops"),
	("engenharia-de-dados"),
	("powerbi"),
	("javascript");
SELECT * FROM tb_categorias tc ;

/*
Nesse caso, como uma postagem pode ter N categorias, e uma categoria pode aparecer em N postagens,
temos uma relação do tipo Muitos-para-muitos (N:N). Para conseguirmos estabelecer essa relação, precisamos
criar uma tabela intermediária, comumente chamada de tabela associativa (fará a associação entre
os registros das 2 tabelas). Geralmente essa tabela possui apenas as chaves estrangeiras das
tabelas associadas.
 */

-- Criação da tabela tb_postagens_categorias
CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
	postagem_id INTEGER NOT NULL,
	categoria_id INTEGER NOT NULL,
	PRIMARY KEY(postagem_id, categoria_id),
	FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
	FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
);

INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES
	(1, 1),
	(1, 2),
	(2, 1),
	(2, 5),
	(3, 1),
	(4, 1),
	(4, 10);

-- Na tabela tb_postagens_categorias, criamos uma chave primária composta, ou seja, uma
-- chave primária que é criada com mais de 1 coluna. Nesse caso, para a regra de chave
-- primária ser aplicada, todas as partes da chave devem se repetir. Por exemplo, o comando
-- abaixo irá falhar, pois já existe uma linha onde os valores das colunas chave primária
-- são 1 1
INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES (1, 1);

-- Agora conseguimos buscar a informação que desejamos. Por exemplo, mostrar todas as
-- postagens que estão na categoria 'programacao'

SELECT tp.id, tp.titulo, tp.data_hora, tc.nome AS "categoria" FROM tb_postagens tp
INNER JOIN tb_postagens_categorias tpc
ON tp.id = tpc.postagem_id 
INNER JOIN tb_categorias tc 
ON tpc.categoria_id = tc.id 
WHERE tc.id = 1;

-- DESAFIO
-- Criar a tabela tb_comentarios, que deve ter a seguinte estrutura
-- id (chave primaria auto incremento)
-- usuario_id (usuario_id que fez o comentário, relacionar com a tb_usuarios)
-- postagem_id (id da postagem a qual pertence esse comentário, relacionar com a tb_postagens)
-- comentario (texto)
-- data_hora (data/hora que o comentário foi realizado, pode seguir o mesmo padrão da tabela tb_postagens)