# pg_waldump

> Display a human-readable rendering of the write-ahead log of a PostgreSQL database cluster.
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Display WAL records from a specific segment:

`pg_waldump {{start_segment}}`

- Display WAL records between two segments:

`pg_waldump {{start_segment}} {{end_segment}}`

- Follow WAL in real-time:

`pg_waldump {{start_segment}} {{[-f|--follow]}}`

- Display records with full page images:

`pg_waldump {{start_segment}} {{[-w|--fullpage]}}`

- Display summary statistics instead of individual records:

`pg_waldump {{start_segment}} {{[-z|--stats]}}`

- Display help:

`pg_waldump {{[-?|--help]}}`

- Display version:

`pg_waldump {{[-V|--version]}}`
