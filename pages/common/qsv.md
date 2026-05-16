# qsv

> A high-performance CSV data-wrangling toolkit written in Rust.
> The spiritual successor to `xsv`.
> More information: <https://github.com/dathere/qsv>.

- Inspect the headers of a CSV file:

`qsv headers {{path/to/file.csv}}`

- Count the number of records:

`qsv count {{path/to/file.csv}}`

- Get per-column statistics, formatted as a table:

`qsv stats {{path/to/file.csv}} | qsv table`

- Select columns by name (in the given order):

`qsv select {{column1,column2}} {{path/to/file.csv}}`

- Show a random sample of records:

`qsv sample {{10}} {{path/to/file.csv}}`

- Filter rows whose column matches a `regex`:

`qsv search --select {{column}} {{pattern}} {{path/to/file.csv}}`

- Show the most frequent values in a column:

`qsv frequency --select {{column}} --limit {{5}} {{path/to/file.csv}}`

- Join two CSV files on a column:

`qsv join {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}}`
