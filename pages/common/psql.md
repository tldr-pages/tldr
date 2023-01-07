# psql

> PostgreSQL command-line client.
> More information: <https://www.postgresql.org/docs/current/app-psql.html>.

- Connect to the database. By default, it connects to the local socket using port 5432 with the currently logged in user:

`psql {{database}}`

- Connect to the database on given server host running on given port with given username, without a password prompt:

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Connect to the database; user will be prompted for password:

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- Execute a single SQL query or PostgreSQL command on the given database (useful in shell scripts):

`psql -c '{{query}}' {{database}}`

- Execute commands from a file on the given database:

`psql {{database}} -f {{file.sql}}`
