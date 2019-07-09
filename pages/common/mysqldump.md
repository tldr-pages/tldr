# mysqldump

> Backups MySQL databases.
> More information: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Create a backup, user will be prompted for a password:

`mysqldump -u {{user}} --password {{database_name}} -r {{filename.sql}}`

- Restore a backup, user will be prompted for a password:

`mysql -u {{user}} --password -e "source {{filename.sql}}" {{database_name}}`

- Backup all databases redirecting the output to a file (user will be prompted for a password):

`mysqldump -u {{user}} -p --all-databases > {{filename.sql}}`

- Restore all databases from a backup (user will be prompted for a password):

`mysql -u {{user}} -p < {{filename.sql}}`
