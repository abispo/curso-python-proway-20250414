# Versionamento de banco de dados utilizando alembic
Alembic é uma ferramenta que permite realizar alterações na estrutura do banco de dados utilizando apenas código, por meio de arquivos que chamamos de `migrations`. Quando trabalhamos com ORMs (independentemente da linguagem), essa é a maneira comum de lidar com alterações na estrutura das tabelas.

## Instalação e uso
Instalamos o alembic simplesmente utilizando o `pip`: `pip install alembic`. Depois disso, precisamos criar a estrutura de pastas do alembic com o comando `alembic init alembic` (`alembic.exe` se estiver no windows). Esse comando vai criar a pasta `alembic` no diretório raiz do projeto, com a seguinte estrutura:
* `alembic.ini`: Esse arquivo é criado no mesmo nível da pasta `alembic`, se serve para armazenar as configurações.
* `alembic/env.py`: É o arquivo utilizado na hora de executar qualquer comando do alembic. A partir desse arquivo podemos alterar configurações carregadas no `alembic.ini`
* `alembic/README`: Arquivos README comum
* `alembic/script.py.mako`: É o template utilizado na geração dos arquivos de migrations. Qualquer alteração feita nesse arquivo, será incluída em todas as migrations geradas.
* `alembic/versions/`: É o diretório onde os arquivos de migrations serão armazenados.

Após alterar uma model, executamos o comando `alembic revision --autogenerate --message "[mensagem]"`. Caso a autogeração de migrations estiver ativada (está no nosso caso), o alembic vai consultar o banco de dados e comparar as tabelas com a estrutura de models. Se houver diferença, é gerado um arquivo de migration. O nome desse arquivo gerá a concateção de um código randômico, com a mensagem informada em `[mensagem]`. Após ser revisado, podemos aplicar essas alterações no banco de dados utilizando o comando `alembic upgrade head`, que irá aplicar sempre a última migration gerada.

# Desafios

## Completar o schema da base de blog
Criar a model `Comentario`, que representa um comentário feito em uma postagem. A tabela mapeada pra essa model deve ter o nome de comentario, e as seguintes colunas:
* `id` (int, chave primária, auto incremento)
* `usuario_id` (int, chave estrangeira pra usuarios.id, não nulo)
* `postagem_id` (int, chave estrangeira pra postagens.id, não nulo)
* `texto` (string de tamanho máximo 200, não nulo)
* `criado_em` (datetime que será criado no momento que o comentário for salvo)

### Bônus
Finalizar a estrutura (funções e lógica) de criação, consulta, atualização e remoção de usuários e das outras entidades do sistema de blog.

## Criar uma base de dados de cursos e alunos
Utilizando SQLAlchemy, você irá criar toda a estrutura de tabelas de um curso fictício. Você irá armazenar dados de `alunos`, `instrutores`, `cursos` e `turmas`. Nesse caso, sinta-se a vontade para criar essa estrutura da maneira que achar adequada (porém, levando em conta o aprendizado das aulas anteriores: relacionamentos, normalização, etc). Depois será mostrada uma versão pronta para comparação.