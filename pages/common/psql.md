# psql

> PostgreSQL client.
> More information: <https://www.postgresql.org/docs/current/app-psql.html>.

- Connect to the database. By default, it connects to the local socket using port 5432 with the currently logged in user:

`psql {{database_name}}`

- Connect to the database on given server host running on given port with given username, without a password prompt:

`psql {{database_name}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Connect to the database; user will be prompted for password:

`psql {{database_name}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-W|--password]}}`

- Execute a single SQL query or PostgreSQL command on the given database (useful in shell scripts):

`psql {{database_name}} {{[-c|--command]}} '{{query}}'`

- Execute commands from a file on the given database:

`psql {{database_name}} {{[-f|--file]}} {{path/to/input_file.sql}}`
