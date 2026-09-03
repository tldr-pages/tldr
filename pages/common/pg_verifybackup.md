# pg_verifybackup

> Verify the integrity of a base backup of a PostgreSQL cluster.
> More information: <https://www.postgresql.org/docs/current/app-pgverifybackup.html>.

- Verify a backup stored in a specific directory:

`pg_verifybackup {{path/to/backup_directory}}`

- Verify a backup showing progress information:

`pg_verifybackup {{path/to/backup_directory}} {{[-P|--progress]}}`

- Verify a backup and exit immediately on first error:

`pg_verifybackup {{path/to/backup_directory}} {{[-e|--exit-on-error]}}`

- Verify a backup ignoring specific files or directories:

`pg_verifybackup {{path/to/backup_directory}} {{[-i|--ignore]}} {{path/to/file_or_directory}}`

- Verify a backup with a manifest file in a different location:

`pg_verifybackup {{path/to/backup_directory}} {{[-m|--manifest-path]}} {{path/to/backup_manifest}}`

- Display help:

`pg_verifybackup {{[-?|--help]}}`
