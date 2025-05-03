# Desafios

## Completar o schema da base de blog
Criar a model Comentario, que representa um comentário feito em uma postagem. A tabela mapeada pra essa model deve ter o nome de comentario, e as seguintes colunas:
* id (int, chave primária, auto incremento)
* usuario_id (int, chave estrangeira pra usuarios.id, não nulo)
* postagem_id (int, chave estrangeira pra postagens.id, não nulo)
* texto (string de tamanho máximo 200, não nulo)
* criado_em (datetime que será criado no momento que o comentário for salvo)

## Criar uma base de dados de cursos e alunos
Utilizando SQLAlchemy, você irá criar toda a estrutura de tabelas de um curso fictício. Você irá armazenar dados de alunos, instrutores, cursos e turmas. Nesse caso, sinta-se a vontade para criar essa estrutura da maneira que achar adequada (porém, levando em conta o aprendizado das aulas anteriores: relacionamentos, normalização, etc). Depois será mostrada uma versão pronta para comparação.