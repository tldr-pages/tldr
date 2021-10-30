# pg_dump

> Extract a PostgreSQL database into a script file or other archive file.
> More information: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Dump database into an SQL-script file:

`pg_dump {{db_name}} > {{output_file.sql}}`

- Same as above, customize username:

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- Same as above, customize host and port:

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- Dump a database into a custom-format archive file:

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`

- Dump only database data into an SQL-script file:

`pg_dump -a {{db_name}} > {{path/to/output_file.sql}}`

- Dump only schema (data definitions) into an SQL-script file:

`pg_dump -s {{db_name}} > {{path/to/output_file.sql}}`
