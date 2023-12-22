# mysql

> A ferramenta de linha de comando do MySQL.
> Mais informações: <https://www.mysql.com/>.

- Conecta a um banco de dados:

`mysql {{nome_do_banco_de_dados}}`

- Conecta a um banco de dados (será solicitada a senha de acesso do usuário):

`mysql -u {{usuário}} --password {{nome_do_banco_de_dados}}`

- Conecta a um banco de dados disponível em um endereço específico:

`mysql -h {{endereco_do_banco_de_dados}} {{nome_do_banco_de_dados}}`

- Conecta a um banco de dados utilizando um socket Unix:

`mysql --socket {{caminho/para/socket.sock}}`

- Executa todos os comandos de um arquivo SQL em um banco de dados:

`mysql -e "source {{nome_do_arquivo.sql}}" {{nome_do_banco_de_dados}}`
