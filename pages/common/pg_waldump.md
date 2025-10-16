# pg_waldump

> Display a human-readable rendering of the write-ahead log (WAL).
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Basic invocation reading a WAL segment (or range):

`pg_waldump {{start_segment}} {{end_segment}}`

- Specify the WAL file directory:

`pg_waldump {{start_segment}} {{end_segment}} {{[-p|--path]}} {{path}}`

- Start from a particular WAL location (LSN):

`pg_waldump {{start_segment}} {{end_segment}} {{[-s|--start]}} {{lsn}}`

- Stop at a particular WAL location (LSN):

`pg_waldump {{start_segment}} {{end_segment}} {{[-e|--end]}} {{lsn}}`

- Follow new WAL entries as they arrive:

`pg_waldump {{start_segment}} {{end_segment}} {{[-f|--follow]}}`

- Limit number of records shown:

`pg_waldump {{start_segment}} {{end_segment}} {{[-n|--limit]}} {{count}}`

- Quiet mode (suppress output except errors):

`pg_waldump {{start_segment}} {{end_segment}} {{[-q|--quiet]}}`

- Filter by resource manager:

`pg_waldump {{start_segment}} {{end_segment}} {{[-r|--rmgr]}} {{rmgr_name}}`
