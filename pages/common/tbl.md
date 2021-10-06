# tbl

> Format tables for `troff`.
> More information: <https://manned.org/tbl>.

- Format tables for `troff` and print it to stdout:

`cat {{path/to/file.troff}} | tbl`

- Format tables for `troff` in "compatibility mode":

`cat {{path/to/file.troff}} | tbl -C`

- Format tables for `troff` from a file:

`tbl {{path/to/file.troff}}`

- Mark the beginning of a table ("Table Start"):

`.TS`

- Mark the end of the table ("Table End"):

`.TE`
