# qsv

> Blazing-fast toolkit for querying, slicing, sorting, analyzing, filtering, transforming, and validating tabular data.
> More information: <https://qsv.dathere.com/>.

- Count the rows in a CSV file:

`qsv count {{path/to/file.csv}}`

- Select specific columns from a CSV file:

`qsv select {{column1,column2,...}} {{path/to/file.csv}}`

- Filter rows containing a regex or literal text:

`qsv search {{regex_or_text}} {{path/to/file.csv}}`

- Sort a CSV file by one or more columns:

`qsv sort {{column1,column2,...}} {{path/to/file.csv}}`

- Compute summary statistics and infer data types for each column:

`qsv stats {{path/to/file.csv}}`

- Display help:

`qsv --help`

- Display version:

`qsv --version`
