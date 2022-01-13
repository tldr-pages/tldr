# pg_dumpall

> Extract a PostgreSQL database cluster into a script file or other archive file.
> More information: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- Dump all databases:

`pg_dumpall > {{path/to/file.sql}}`

- Dump all databases using a specific username:

`pg_dumpall --username={{username}} > {{path/to/file.sql}}`

- Same as above, customize host and port:

`pg_dumpall -h {{host}} -p {{port}} > {{output_file.sql}}`

- Dump all databases into a custom-format archive file with moderate compression:

`pg_dumpall -Fc > {{output_file.dump}}`

- Dump only database data into an SQL-script file:

`pg_dumpall --data-only > {{path/to/file.sql}}`

- Dump only schema (data definitions) into an SQL-script file:

`pg_dumpall -s > {{output_file.sql}}`
