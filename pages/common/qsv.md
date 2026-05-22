# qsv

> A CSV data wrangling toolkit written in Rust.
> More information: <https://qsv.dathere.com/>.

- Inspect the headers of a file:

`qsv headers {{path/to/file.csv}}`

- Count the number of records:

`qsv count {{path/to/file.csv}}`

- Display summary statistics in a table:

`qsv stats {{path/to/file.csv}} | qsv table`

- Select specific columns:

`qsv select {{column1,column2}} {{path/to/file.csv}}`

- Show 10 random records:

`qsv sample {{10}} {{path/to/file.csv}}`

- Join a column from one file to another:

`qsv join --ignore-case {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}} | qsv table`
