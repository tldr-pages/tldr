# mysql

> The MySQL command-line tool.
> More information: <https://www.mysql.com/>.

- Connect to a database:

`mysql {{database_name}}`

- Connect to a database, user will be prompted for a password:

`mysql -u {{user}} --password {{database_name}}`

- Connect to a database on another host:

`mysql -h {{database_host}} {{database_name}}`

- Connect to a database through a Unix socket:

`mysql --socket {{path/to/socket.sock}}`

- Execute SQL statements in a script file (batch file):

`mysql -e "source {{filename.sql}}" {{database_name}}`
