# mysqldump

> Backups mysql databases

- creating a backup

`mysqldump -u {{user}} -p{{password}} {{database_name}} > {{filename.sql}}`

- restoring a backup

`mysql -u {{user}} -p{{password}} {{database_name}} < {{filename.sql}}`
