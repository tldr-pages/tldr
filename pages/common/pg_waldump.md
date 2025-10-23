# pg_waldump

> Display a human-readable rendering of the write-ahead log (WAL) of a PostgreSQL database cluster.
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Display WAL records from a specific segment:

`pg_waldump {{start_segment}}`

- Display WAL records between two segments:

`pg_waldump {{start_segment}} {{end_segment}}`

- Specify the WAL file directory:

`pg_waldump {{start_segment}} {{end_segment}} {{[-p|--path]}} {{path}}`

- Follow new WAL entries as they arrive:

`pg_waldump {{start_segment}} {{end_segment}} {{[-f|--follow]}}`

- Limit number of records shown:

`pg_waldump {{start_segment}} {{end_segment}} {{[-n|--limit]}} {{count}}`

- Display summary statistics instead of individual records:

`pg_waldump {{start_segment}} {{end_segment}} {{[-z|--stats]}}`

- Filter by resource manager:

`pg_waldump {{start_segment}} {{end_segment}} {{[-r|--rmgr]}} {{rmgr_name}}`

- Display help:

`pg_waldump {{[-?|--help]}}`
