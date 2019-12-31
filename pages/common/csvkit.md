# csvkit

> Manipulation toolkit for CSV files.
> See the individual commands: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
> More information: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- Run a command on a CSV file with a custom delimiter:

`{{cmd}} -d {{delimiter}} {{filename.csv}}`

- Run a command on a CSV file with a tab as a delimiter (overrides -d):

`{{cmd}} -t {{filename.csv}}`

- Run a command on a CSV file with a custom quote character:

`{{cmd}} -q {{quote_char}} {{filename.csv}}`

- Run a command on a CSV file with no header row:

`{{cmd}} -H {{filename.csv}}`
