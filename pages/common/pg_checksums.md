# pg_checksums

> Enable, disable, or check data checksums in a PostgreSQL database cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgchecksums.html>.

- Check data checksums in a database cluster:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data_directory}}`

- Enable data checksums in a database cluster:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-e|--enable]}}`

- Disable data checksums in a database cluster:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-d|--disable]}}`

- Check data checksums with verbose output:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-v|--verbose]}}`

- Check data checksums showing progress:

`pg_checksums {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-P|--progress]}}`

- Display help:

`pg_checksums {{[-?|--help]}}`
