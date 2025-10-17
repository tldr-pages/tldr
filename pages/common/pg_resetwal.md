# pg_resetwal

> Reset the write-ahead log and other control information of a PostgreSQL database cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgresetwal.html>.

- Reset the WAL and control information for a specific data directory:

`pg_resetwal {{[-D|--pgdata]}} {{path/to/data}}`

- Perform a dry run:

`pg_resetwal {{[-n|--dry-run]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Force the WAL and control information reset:

`pg_resetwal {{[-f|--force]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Display help:

`pg_resetwal {{[-?|--help]}}`

- Display version:

`pg_resetwal {{[-V|--version]}}`
