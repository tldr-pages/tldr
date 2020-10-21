# mysql

> Herramienta en línea de comandos para gestionar bases de datos MySQL
> More information: <https://www.mysql.com/>.

- Conectarse a una base de datos:

`mysql {{database_name}}`

- Conectarse a una base de datos con el usuario `user` y se le pedirá una contraseña:

`mysql -u {{user}} --password {{database_name}}`

- Connect to a database on another host:

`mysql -h {{database_host}} {{database_name}}`

- Connect to a database through a Unix socket:

`mysql --socket {{path/to/socket.sock}}`

- Execute SQL statements in a script file (batch file):

`mysql -e "source {{filename.sql}}" {{database_name}}`

- Restore a database from a backup created with `mysqldump` (user will be prompted for a password):

`mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}`

- Restore all databases from a backup (user will be prompted for a password):

`mysql --user {{user}} --password < {{path/to/backup.sql}}`
