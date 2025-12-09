# mysql

> The MySQL tool.
> More information: <https://manned.org/mysql>.

- Connect to a database:

`mysql {{database_name}}`

- Connect to a database, user will be prompted for a password:

`mysql {{[-u|--user]}} {{user}} {{[-p|--password]}} {{database_name}}`

- Connect to a database on another host:

`mysql {{[-h|--host]}} {{database_host}} {{database_name}}`

- Connect to a database through a Unix socket:

`mysql {{[-S|--socket]}} {{path/to/socket.sock}}`

- Execute SQL statements in a script file (batch file):

`mysql {{[-e|--execute]}} "source {{filename.sql}}" {{database_name}}`

- Restore a database from a backup created with `mysqldump` (user will be prompted for a password):

`mysql < {{path/to/backup.sql}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{database_name}}`

- Restore all databases from a backup (user will be prompted for a password):

`mysql < {{path/to/backup.sql}} {{[-u|--user]}} {{user}} {{[-p|--password]}}`
