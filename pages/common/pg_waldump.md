# pg_waldump

> Display a human-readable rendering of PostgreSQL write-ahead log (WAL) files for debugging or analysis.
> More information: <https://www.postgresql.org/docs/current/pgwaldump.html>.

- Display all available WAL records from default paths:

`pg_waldump`

- Display WAL records in a specific segment range:

`pg_waldump {{startseg}} {{endseg}}`

- Filter records by a specific resource manager (e.g., `xlog`):

`pg_waldump -r {{xlog}}`

- Limit output to a specific number of records:

`pg_waldump -n {{100}}`

- Follow and poll for new WAL data every second:

`pg_waldump -f`

- Display summary statistics instead of individual records:

`pg_waldump -z`
