# mysqldump

> Backups MySQL databases.

- Create a backup, user will be prompted for a password:

`mysqldump -u {{user}} --password {{database_name}} -r {{filename.sql}}`

- Restore a backup, user will be prompted for a password:

`mysql -u {{user}} --password {{database_name}} -e "source {{/path/to/backup-file.sql]}" {{database_name}}`
