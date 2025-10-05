# pg_walsummary

> Print contents of WAL summary files.
> More information: <https://www.postgresql.org/docs/current/app-pgwalsummary.html>.

- Convert a WAL summary file to text:

`pg_walsummary {{file}}`

- Print one line per individual modified block (rather than ranges):

`pg_walsummary {{[-i|--individual]}} {{file}}`

- Suppress normal output (only errors):

`pg_walsummary {{[-q|--quiet]}} {{file}}`
