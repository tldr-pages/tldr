# psql

> PostgreSQL command-line client.
> More information: <https://www.postgresql.org/docs/current/app-psql.html>.

- Connect to the database. It connects to localhost using default port 5432 with default user as currently logged in user:

`psql {{database}}`

- Connect to the database on given server host running on given port with given username, without a password prompt:

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Connect to the database; user will be prompted for password:

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- Execute commands from a file on the given database:

`psql {{database}} -f {{file.sql}}`

- Select all items in a given table:

`psql -c 'SELECT * FROM {{table}};' {{database}}`

- Update all items under certain conditions:

`psql -c 'UPDATE {{table}} SET ({{column1}}, {{column2}}) = ({{value1}}, {{value2}}) WHERE {{condition}};' {{database}}`

- Insert new items:

`psql -c 'INSERT INTO {{table}} ({{column1}}, {{column2}}) VALUES ({{value1}}, {{value2}});' {{database}}`

- Delete items under certain conditions:

`psql -c 'DELETE FROM {{table}} WHERE {{condition}};' {{database}}`
