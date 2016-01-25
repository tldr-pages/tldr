# mysqldump

> Backups mysql databases.

- Create a backup, user will be prompted for a password:

`mysqldump -u {{user}} --password {{database_name}} > {{filename.sql}}`

- Restore a backup, user will be prompted for a password:

`mysql -u {{user}} --password {{database_name}} < {{filename.sql}}`
