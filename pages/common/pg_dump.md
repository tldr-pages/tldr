# pg_dump

> Extract a PostgreSQL database into a script file or other archive file.

- Dump database into a SQL-script file:

`pg_dump {{db_name}} > {{output_file.sql}}`

- Same as above, customize username:

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- Same as above, customize host and port:

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- Dump a database into a custom-format archive file:

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`
