# pg_archivecleanup

> Remove old WAL archive files in PostgreSQL.
> More information: <https://www.postgresql.org/docs/current/pgarchivecleanup.html>.

- Clean an archive directory up to a given WAL file:

`pg_archivecleanup {{path/to/archive_directory}} {{path/to/wal_file}}`

- Perform a dry run (list files that would be removed without actually doing it):

`pg_archivecleanup {{path/to/archive_directory}} {{path/to/wal_file}} {{[-n|--dry-run]}}`

- Strip a file extension before deciding deletion:

`pg_archivecleanup {{path/to/archive_directory}} {{path/to/wal_file}} {{[-x|--strip-extension]}} {{extension}}`

- Remove backup history files too:

`pg_archivecleanup {{path/to/archive_directory}} {{path/to/wal_file}} {{[-b|--clean-backup-history]}}`

- Enable debug logging output:

`pg_archivecleanup {{path/to/archive_directory}} {{path/to/wal_file}} {{[-d|--debug]}}`
