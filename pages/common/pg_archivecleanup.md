# pg_archivecleanup

> Remove old WAL archive files in PostgreSQL.
> More information: <https://www.postgresql.org/docs/current/pgarchivecleanup.html>.

- Clean an archive directory up to a given WAL file:

`pg_archivecleanup {{path/to/archive}} {{path/to/walfile}}`

- Perform a dry run (list files that would be removed without actually doing it):

`pg_archivecleanup {{[-n|--dry-run]}} {{path/to/archive}} {{path/to/walfile}}`

- Strip a file extension before deciding deletion:

`pg_archivecleanup {{[-x|--strip-extension]}} {{extension}} {{path/to/archive}} {{path/to/walfile}}`

- Remove backup history files too:

`pg_archivecleanup {{[-b|--clean-backup-history]}} {{path/to/archive}} {{path/to/walfile}}`

- Enable debug logging output:

`pg_archivecleanup {{[-d|--debug]}} {{path/to/archive}} {{path/to/walfile}}`
