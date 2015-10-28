# psql

> PostgreSQL command-line client

- Connect to *database*. It connects to localhost using default port *5432* with default user

`psql {{database}}`

- Connect to *database* on given server *host* running on given *port* with *username* given

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Run single *query* against the given *database*. Note: useful in shell scripts

`psql -c '{{query}}' {{database}}`

- Run several queries against the given *database*. Note: useful in shell scripts

`echo '{{query1}}; {{query2}}' | psql {{database}}`
