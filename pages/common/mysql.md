# mysql

> the MySQL command-line tool

- Connect to a database

`mysql {{database_name}}`

- Connect to a database using credentials

`mysql -h {{database_host}} -u {{user}} -p{{password}} {{database_name}}`

- Connect to a database on a different host. MySQL will prompt for a password if none is supplied.

`mysql -h {{database_host}} -u {{user}} -p {{database_name}}`

- Execute SQL statements in a script file (batch file)

`mysql {{database_name}} < {{script.sql}}`
