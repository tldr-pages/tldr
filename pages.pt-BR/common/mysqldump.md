# mysqldump

> Realizar e restaurar backups no MySQL.
> Página oficial: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Criar o backup de um banco de dados específico em arquivo de saída, será solicitada a senha de acesso do usuário informado:

`mysqldump -u {{usuário}} --password {{nome_do_banco_de_dados}} -r {{arquivo_de_saida.sql}}`

- Restaurar o conteúdo contido no arquivo de backup em banco de dados específico, será solicitada a senha de acesso do usuário informado:

`mysql -u {{usuário}} --password -e "source {{arquivo_de_backup.sql}}" {{nome_do_banco_de_dados}}`
