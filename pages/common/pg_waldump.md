# pg_waldump

> Display a human-readable rendering of the write-ahead log (WAL).
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Basic invocation reading a WAL segment (or range):

`pg_waldump {{startseg}} {{endseg}}`

- Specify the WAL file directory:

`pg_waldump {{startseg}} {{endseg}} {{[-p|--path]}} {{path}}`

- Start from a particular WAL location (LSN):

`pg_waldump {{startseg}} {{endseg}} {{[-s|--start]}} {{lsn}}`

- Stop at a particular WAL location (LSN):

`pg_waldump {{startseg}} {{endseg}} {{[-e|--end]}} {{lsn}}`

- Follow new WAL entries as they arrive:

`pg_waldump {{startseg}} {{endseg}} {{[-f|--follow]}}`

- Limit number of records shown:

`pg_waldump {{startseg}} {{endseg}} {{[-n|--limit]}} {{count}}`

- Quiet mode (suppress output except errors):

`pg_waldump {{startseg}} {{endseg}} {{[-q|--quiet]}}`

- Filter by resource manager:

`pg_waldump {{startseg}} {{endseg}} {{[-r|--rmgr]}} {{rmgr_name}}`
