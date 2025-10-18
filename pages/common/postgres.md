# postgres

> Run the PostgreSQL database server.
> More information: <https://www.postgresql.org/docs/current/app-postgres.html>.

- Start the server on a specific port:

`postgres -p {{1234}}`

- Set a runtime parameter (short form):

`postgres -c {{work_mem=1234}}`

- Set a runtime parameter (long form):

`postgres --{{work_mem}}={{1234}}`

- Start in single-user mode for a specific database:

`postgres --single -D {{path/to/datadir}} {{my_database}}`
