# [mysql](http://man7.org/linux/man-pages/man1/mysql.1.html)
> The MySQL command-line tool.

- Connect to a database:

`mysql {{database_name}}`

- Connect to a database, user will be prompted for a password:

`mysql -u {{user}} --password {{database_name}}`

- Connect to a database on another host:

`mysql -h {{database_host}} {{database_name}}`

- Execute SQL statements in a script file (batch file):

`mysql {{database_name}} < {{script.sql}}`
