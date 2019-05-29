# pg_restore

> Restore a PostgreSQL database from an archive file created by pg_dump.
> More information: <https://www.postgresql.org/docs/current/app-pgrestore.html>.

- Restore an archive into an existing database:

`pg_restore -d {{db_name}} {{archive_file.dump}}`

- Same as above, customize username:

`pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}`

- Same as above, customize host and port:

`pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}`

- Clean database objects before creating them:

`pg_restore --clean -d {{db_name}} {{archive_file.dump}}`

- Use multiple jobs to do the restoring:

`pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}`
