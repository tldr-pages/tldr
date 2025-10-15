# pg_verifybackup

> Verify the integrity of a base backup of a PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgverifybackup.html>.

- Verify a backup stored in a specific directory:

`pg_verifybackup {{path/to/backup}}`

- Verify a backup showing progress information:

`pg_verifybackup {{[-P|--progress]}} {{path/to/backup}}`

- Verify a backup and exit immediately on first error:

`pg_verifybackup {{[-e|--exit-on-error]}} {{path/to/backup}}`

- Verify a backup ignoring specific files or directories:

`pg_verifybackup {{[-i|--ignore]}} {{path/to/file_or_directory}} {{path/to/backup}}`

- Verify a backup with a manifest file in a different location:

`pg_verifybackup {{[-m|--manifest-path]}} {{path/to/backup_manifest}} {{path/to/backup}}`

- Display help:

`pg_verifybackup {{[-?|--help]}}`
