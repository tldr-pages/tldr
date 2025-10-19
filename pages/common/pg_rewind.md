# pg_rewind

> Synchronize a PostgreSQL data directory with another data directory that was forked from it.
> More information: <https://www.postgresql.org/docs/current/app-pgrewind.html>.

- Synchronize target directory with source directory:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}}`

- Synchronize target with source server using connection string:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-server {{connstr}}`

- Perform a dry run:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}} {{[-n|--dry-run]}}`

- Show progress during synchronization:

`pg_rewind {{[-D|--target-pgdata]}} {{path/to/target_data}} --source-pgdata {{path/to/source_data}} {{[-P|--progress]}}`

- Display help:

`pg_rewind {{[-?|--help]}}`
