# mysqldump

> Backups MySQL databases.
> More information: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Create a backup, user will be prompted for a password:

`mysqldump -u {{user}} --password {{database_name}} -r {{filename.sql}}`

- Restore a backup, user will be prompted for a password:

`mysql -u {{user}} --password -e "source {{filename.sql}}" {{database_name}}`

- Backup all databases with compression, user will be prompted for a password:

`mysqldump -u {{user}} -p --all-databases | gzip > {{filename.sql.gz}}`

- Restore a compressed database backup, user will be prompted for a password:

`gunzip -c {{filename.sql.gz}} | mysql -u {{user}} -p`
