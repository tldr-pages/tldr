# pg_dump

> Extract a PostgreSQL database into a script file or other archive file.
> More information: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Dump database into an SQL-script file:

`pg_dump {{database_name}} > {{path/to/output_file.sql}}`

- Same as above, customize username:

`pg_dump {{database_name}} {{[-U|--username]}} {{username}} > {{path/to/output_file.sql}}`

- Same as above, customize host and port:

`pg_dump {{database_name}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} > {{path/to/output_file.sql}}`

- Dump a database into a custom-format archive file:

`pg_dump {{database_name}} {{[-F|--format]}} {{[c|custom]}} > {{path/to/output_file.dump}}`

- Dump only database data into an SQL-script file:

`pg_dump {{database_name}} {{[-a|--data-only]}} > {{path/to/output_file.sql}}`

- Dump only schema (data definitions) into an SQL-script file:

`pg_dump {{database_name}} {{[-s|--schema-only]}} > {{path/to/output_file.sql}}`
