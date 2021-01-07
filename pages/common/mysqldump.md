# mysqldump

> Backups MySQL databases.
> See also `mysql` for restoring databases.
> More information: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Create a backup (user will be prompted for a password):

`mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}`

- Backup a specific table redirecting the output to a file (user will be prompted for a password):

`mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}`

- Backup all databases redirecting the output to a file (user will be prompted for a password):

`mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}`

- Backup all databases from a remote host, redirecting the output to a file (user will be prompted for a password):

`mysqldump --host={(ip_or_hostname)} --user {{user}} --password --all-databases > ({path/to/file.sql}}`
