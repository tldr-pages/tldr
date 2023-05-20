# csvkit

> Manipulation toolkit for CSV files.
> See also: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
> More information: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- Run a command on a CSV file with a custom delimiter:

`{{command}} -d {{delimiter}} {{path/to/file.csv}}`

- Run a command on a CSV file with a tab as a delimiter (overrides -d):

`{{command}} -t {{path/to/file.csv}}`

- Run a command on a CSV file with a custom quote character:

`{{command}} -q {{quote_char}} {{path/to/file.csv}}`

- Run a command on a CSV file with no header row:

`{{command}} -H {{path/to/file.csv}}`
