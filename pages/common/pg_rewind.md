# pg_rewind

> Synchronize a PostgreSQL data directory with another after their timelines diverge (e.g., after failover).
> More information: <https://www.postgresql.org/docs/current/app-pgrewind.html>.

- Synchronize from a source data directory:

`pg_rewind -D {{path/to/target/pgdata}} --source-pgdata={{path/to/source/pgdata}}`

- Synchronize from a running source server via connection string:

`pg_rewind -D {{path/to/target/pgdata}} --source-server='{{host=sourcehost dbname=postgres}}'`

- Perform a dry run without applying changes:

`pg_rewind -D {{path/to/target/pgdata}} --source-pgdata={{path/to/source/pgdata}} -n`

- Restore missing WAL files from the target's archive during rewind:

`pg_rewind -D {{path/to/target/pgdata}} --source-pgdata={{path/to/source/pgdata}} -c`

- Set up recovery configuration in the target and show progress:

`pg_rewind -D {{path/to/target/pgdata}} --source-server='{{host=sourcehost dbname=postgres}}' -R -P`
