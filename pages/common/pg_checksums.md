# pg_checksums

> Enable, disable, or check data checksums in a PostgreSQL database cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgchecksums.html>.

- Check data checksums in a database cluster:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data}}`

- Enable data checksums in a database cluster:

`pg_checksums {{[-e|--enable]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Disable data checksums in a database cluster:

`pg_checksums {{[-d|--disable]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Check data checksums with verbose output:

`pg_checksums {{[-v|--verbose]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Check data checksums showing progress:

`pg_checksums {{[-P|--progress]}} {{[-D|--pgdata]}} {{path/to/data}}`

- Display help:

`pg_checksums {{[-?|--help]}}`
