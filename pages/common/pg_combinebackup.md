# pg_combinebackup

> Reconstruct a full (synthetic) PostgreSQL backup from an incremental backup chain.
> When specifying multiple backups order them from oldest to newest.
> More information: <https://www.postgresql.org/docs/current/app-pgcombinebackup.html>.

- Combine a full and incremental backup into one synthetic full backup:

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}}`

- Perform a dry run to show what would be done, without creating files:

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}} {{[-n|--dry-run]}}`

- Use hard links instead of copying files (faster, same filesystem required):

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}} {{[-k|--link]}}`

- Use file cloning (reflinks) for efficient copy if supported:

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}} --clone`

- Use the `copy_file_range` system call for efficient copying:

`pg_combinebackup {{path/to/full_backup}} {{path/to/incremental_backup}} {{[-o|--output]}} {{path/to/output_directory}} --copy-file-range`

- Relocate a tablespace during reconstruction:

`pg_combinebackup {{path/to/backup1 path/to/backup2 ...}} {{[-T|--tablespace-mapping]}} /{{path/to/old_tablespace}}=/{{path/to/new_tablespace}} {{[-o|--output]}} {{path/to/output_directory}}`

- Disable fsync for faster but unsafe writes (testing only):

`pg_combinebackup {{path/to/backup1 path/to/backup2 ...}} {{[-o|--output]}} {{path/to/output_directory}} {{[-N|--no-sync]}}`

- Show detailed debug output:

`pg_combinebackup {{path/to/backup1 path/to/backup2 ...}} {{[-o|--output]}} {{path/to/output_directory}} {{[-d|--debug]}}`
