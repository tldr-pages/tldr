# csvkit

> Manipulation toolkit for CSV files.
> More information: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- Run a command on a CSV file with the non default delimiter:

`{{cmd}} -d {{delimiter}} {{filename.csv}}`

- Run a command on a CSV file with a tab as a delimiter (overides -d):

`{{cmd}} -t {{filename.csv}}`

- Run a command on a CSV file with the non default quote character:

`{{cmd}} -q {{quote_char}} {{filename.csv}}`

- Run a command on a CSV file with no header row:

`{{cmd}} -H {{filename.csv}}`
