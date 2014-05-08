# psql

> PostgreSQL command-line client

- Connect to database. It connects to localhost using default port *5432* with default user.

`psql {{database}}`

- Connect to database on given server host running on given port with username given

`psql -h {{host}} -p {{port}} -U {{username}} mydb`

- Run query against the given database

`echo '{{query}}' | psql {{database}}`

or

`psql -c '{{query}}' {{database}}`
