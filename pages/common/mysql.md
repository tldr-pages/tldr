# mysql

> the MySQL command-line tool

- Connect to a database

`mysql {{database_name}}`

- Connect to a database, user will be prompted for a password

`mysql -u {{user}} --password {{database_name}}`

- Execute SQL statements in a script file (batch file)

`mysql {{database_name}} < {{script.sql}}`
