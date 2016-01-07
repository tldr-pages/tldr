# mysql

> the MySQL command-line tool

- Connect to a database

`mysql {{database_name}}`

- Connect to a database using credentials

`mysql -u {{user}} -p{{password}} {{database_name}}`

- Connect to a database on another host

`mysql -h {{database_host}}

- Execute SQL statements in a script file (batch file)

`mysql {{database_name}} < {{script.sql}}`
