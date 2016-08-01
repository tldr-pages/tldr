# psql

> PostgreSQL command-line client.

- Connect to database. It connects to localhost using default port 5432 with default user:

`psql {{database}}`

- Connect to database on given server host running on given port with username given, no password prompt:

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Connect to database, user will be prompted for password:

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- Execute a single command(sql or internal) against the given database. Note: useful in shell scripts:

`psql -c '{{query}}' {{database}}`

- Execute commands from a file against the given database:

`psql {{database}} -f {{file.sql}}`
