# Relacionamentos entre tabelas em um banco de dados

* 1:1 (Um para um)
* 1:N (Um para muitos)
* N:N (Muitos para muitos)

# Exercícios

## Crie o banco de dados modulo02_exercicios_relacionamentos, e execute lá os seguintes exercícios

1. Crie 2 tabelas: `tb_livros` e `tb_detalhes_livros`. Essas tabelas devem ter um relacionamento `1:1` entre elas. A estrutura das tabelas deve ser a seguinte:

    `tb_livros`
    * id
    * nome
    * autor
    * isbn

    `tb_detalhes_livros`
    * id
    * categoria
    * numero_de_paginas
    * ano_de_lancamento

2. Crie 2 tabelas: `tb_pacientes` e `tb_detalhes_pacientes`. Essas tabelas devem ter um relacionamento `1:1` entre elas. A estrutura das tabelas deve ser a seguinte:

    `tb_pacientes`
    * id
    * nome
    * data_de_nascimento
    * genero

    `tb_detalhes_pacientes`
    * id
    * estado_civil
    * numero_de_filhos
    * fumante

3.  Crie 2 tabelas: `tb_clientes` e `tb_pedidos`. Cada cliente pode fazer diversos pedidos, mas cada pedido está associado a apenas 1 cliente. Defina um relacionamento `1:N` entre essas tabelas. A estrutura das tabelas será a seguinte:
    
    `tb_clientes`
    * id
    * nome
    * data_de_nascimento
    * genero

    `tb_pedidos`
    * id
    * observacoes
    * data_hora

5. Crie 2 tabelas: `tb_usuarios` e `tb_playlists`. Cada usuário pode criar múltiplas playlists, Mas cada playlist pertence a apenas 1 usuário. Defina um relacionamento `1:N`.

    `tb_usuarios`
    * id
    * nome
    * data_de_nascimento
    * genero_favorito

    `tb_playlists`
    * id
    * observacoes
    * data_hora

6. Crie tabelas para hóspedes e reservas. Cada hóspede pode ter muitas reservas, Mas cada reserva está associada a apenas 1 hóspede. Defina um relacionamento `1:N`.
7. Considere o seguinte cenário: Uma universidade oferece diversos cursos, e cada curso pode ter múltiplos estudantes. Além disso, um estudante pode estar associado a diversos cursos. Faça o design das tabelas que represente essa relação `N:N`.
8. Uma loja vende vários produtos, e cada produto pode ser comprado por múltiplos clientes. Um cliente pode comprar vários produtos. Crie as tabelas representando essa relação `N:N`.