# mysql

> A ferramenta de linha de comando do MySQL.
> Página oficial: <https://www.mysql.com/>.

- Conectar ao banco de dados informado:

`mysql {{nome_do_banco_de_dados}}`

- Conectar ao banco de dados informado, será solicitada a senha de acesso do usuário informado:

`mysql -u {{usuário}} --password {{nome_do_banco_de_dados}}`

- Conectar ao banco de dados informado disponível em um endereço específico:

`mysql -h {{endereco_do_banco_de_dados}} {{nome_do_banco_de_dados}}`

- Conectar ao banco de dados utilizando um socket Unix:

`mysql --socket {{caminho/para/socket.sock}}`

- Executar, no banco de dados informado, todos os comandos contidos no arquivo SQL:

`mysql -e "source {{nome_do_arquivo.sql}}" {{nome_do_banco_de_dados}}`
