# csvquote

> Enables common utilities such as `cut` and `awk` to work correctly with CSV files containing quoted delimiters and newlines.
> More information: <https://github.com/dbro/csvquote>.

- Replace quoted special characters in a normal CSV file:

`csvquote {{path/to/data.csv}}`

- Replace quoted special characters in a normal TSV file:

`csvquote -t {{path/to/data.csv}}`

- Restore quoted special characters from stdin:

`csvquote -u`

- Quoting an CSV file for `command` and unquoting after processing (Most Common Use Case):

`csvquote {{path/to/data.csv}} | {{command}} | csvquote -u`
