# pg_walsummary

> Print contents of WAL summary files.
> More information: <https://www.postgresql.org/docs/current/app-pgwalsummary.html>.

- Convert a WAL summary file to text:

`pg_walsummary {{path/to/file}}`

- Print one line per individual modified block (rather than ranges):

`pg_walsummary {{[-i|--individual]}} {{path/to/file}}`

- Suppress normal output (only errors):

`pg_walsummary {{[-q|--quiet]}} {{path/to/file}}`
