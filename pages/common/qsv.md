# qsv

> Ultra-fast CSV data-wrangling toolkit.
> More information: <https://github.com/dathere/qsv>.

- Display summary statistics for a CSV file:

`qsv stats {{path/to/file.csv}}`

- Display column headers and their index positions:

`qsv headers {{path/to/file.csv}}`

- Count the total number of records in a CSV file:

`qsv count {{path/to/file.csv}}`

- Select specific columns from a CSV file:

`qsv select {{column_name1,column_name2}} {{path/to/file.csv}}`

- Slice a range of rows:

`qsv slice --start {{10}} --len {{10}} {{path/to/file.csv}}`

- Search records matching a `regex`:

`qsv search "{{regular_expression}}" {{path/to/file.csv}}`

- Compute frequency distributions for columns:

`qsv frequency {{path/to/file.csv}}`

- Join two CSV files on specified columns:

`qsv join {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}}`
