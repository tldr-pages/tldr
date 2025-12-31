# postgres

> Run the PostgreSQL database server.
> More information: <https://www.postgresql.org/docs/current/app-postgres.html>.

- Start the server on a specific port (defaults to 5432):

`postgres -p {{5433}}`

- Set a runtime parameter (short form):

`postgres -c {{shared_buffers=128MB}}`

- Set a runtime parameter (long form):

`postgres --{{shared-buffers}}={{128MB}}`

- Start in single-user mode for a specific database (defaults to the user name):

`postgres --single -D {{path/to/datadir}} {{my_database}}`
