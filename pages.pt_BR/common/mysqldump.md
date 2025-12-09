# mysqldump

> Realizar e restaurar backups no MySQL.
> Mais informações: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Cria o backup do banco de dados em arquivo de saída (será solicitada a senha de acesso do usuário):

`mysqldump -u {{usuário}} --password {{nome_do_banco_de_dados}} -r {{arquivo_de_saida.sql}}`

- Restaura o conteúdo contido no arquivo de backup em banco de dados específico (será solicitada a senha de acesso do usuário):

`mysql -u {{usuário}} --password -e "source {{arquivo_de_backup.sql}}" {{nome_do_banco_de_dados}}`
