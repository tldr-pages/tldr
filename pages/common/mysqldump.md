# [mysqldump](http://man7.org/linux/man-pages/man1/mysqldump.1.html)
> Backups mysql databases.

- Create a backup, user will be prompted for a password:

`mysqldump -u {{user}} --password {{database_name}} > {{filename.sql}}`

- Restore a backup, user will be prompted for a password:

`mysql -u {{user}} --password {{database_name}} < {{filename.sql}}`
