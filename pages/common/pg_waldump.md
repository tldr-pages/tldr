# pg_waldump

> Display a human-readable rendering of the write-ahead log (WAL) of a PostgreSQL cluster (for debugging/inspection purposes).
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Basic invocation reading a WAL segment (or range):

`pg_waldump {{[startseg]}} {{[endseg]}}`

- Specify the WAL file directory:

`pg_waldump {{[-p|--path]}} {{path}} {{[startseg]}} {{[endseg]}}`

- Start from a particular WAL location (LSN):

`pg_waldump {{[-s|--start]}} {{lsn}} {{[startseg]}} {{[endseg]}}`

- Stop at a particular WAL location (LSN):

`pg_waldump {{[-e|--end]}} {{lsn}} {{[startseg]}} {{[endseg]}}`

- Follow new WAL entries as they arrive:

`pg_waldump {{[-f|--follow]}} {{[startseg]}} {{[endseg]}}`

- Limit number of records shown:

`pg_waldump {{[-n|--limit]}} {{count}} {{[startseg]}} {{[endseg]}}`

- Quiet mode (suppress output except errors):

`pg_waldump {{[-q|--quiet]}} {{[startseg]}} {{[endseg]}}`

- Filter by resource manager:

`pg_waldump {{[-r|--rmgr]}} {{rmgr_name}} {{[startseg]}} {{[endseg]}}`
