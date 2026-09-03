# pg_restore

> Restore a PostgreSQL database from an archive file created by pg_dump.
> More information: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- Restore an archive into an existing database:

`pg_restore {{path/to/archive_file.dump}} {{[-d|--dbname]}} {{database_name}}`

- Same as above, customize username:

`pg_restore {{path/to/archive_file.dump}} {{[-d|--dbname]}} {{database_name}} {{[-U|--username]}} {{username}}`

- Same as above, customize host and port:

`pg_restore {{path/to/archive_file.dump}} {{[-d|--dbname]}} {{database_name}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}}`

- List database objects included in the archive:

`pg_restore {{path/to/archive_file.dump}} {{[-l|--list]}}`

- Clean database objects before creating them:

`pg_restore {{path/to/archive_file.dump}} {{[-d|--dbname]}} {{database_name}} {{[-c|--clean]}}`

- Use multiple jobs to do the restoring:

`pg_restore {{path/to/archive_file.dump}} {{[-d|--dbname]}} {{database_name}} {{[-j|--jobs]}} {{2}}`
