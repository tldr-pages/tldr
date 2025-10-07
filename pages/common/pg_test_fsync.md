# pg_test_fsync

> Determine the fastest wal_sync_method on your system.
> More information: <https://www.postgresql.org/docs/current/pgtestfsync.html>.

- Run the default fsync benchmark (5 seconds):

`pg_test_fsync`

- Specify a custom test duration:

`pg_test_fsync {{[-s|--secs-per-test]}} {{seconds}}`

- Use a specific filename (it must be in same file system that the pg_wal directory is or will be placed in):

`pg_test_fsync {{[-f|--filename]}} {{path/to/file}}`
