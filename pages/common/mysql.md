# mysql

> the MySQL command-line tool 

- Connect to database *database_name*

`mysql {{database_name}}`

- Connect to database *database_name* using *user* and *password* credentials.

`mysql -u {{user}} -p{{password}} {{database_name}}`

or

`mysql --user={{user}} --password={{password}} {{database_name}}`

- Execute SQL statements in a script file (batch file)

`mysql {database_name} < script.sql`