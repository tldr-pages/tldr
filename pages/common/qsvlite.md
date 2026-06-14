# qsvlite

> Slim build of the `qsv` CSV toolkit in Rust. Successor to `xsv`.
> More information: <https://github.com/dathere/qsv>.

- Inspect CSV column headers:

`qsvlite headers {{path/to/file.csv}}`

- Select a few columns:

`qsvlite select {{column1,column2}} {{path/to/file.csv}}`

- Filter rows by `regex`, then select a few columns:

`qsvlite search --select {{column}} {{pattern}} {{path/to/file.csv}} | qsvlite select {{column1,column2}}`

- Count number of entries:

`qsvlite count {{path/to/file.csv}}`

- Show summary statistics as a table:

`qsvlite stats {{path/to/file.csv}} | qsvlite table`

- Show 5 random entries:

`qsvlite sample {{5}} {{path/to/file.csv}}`

- Show the most frequent 5 values in a column:

`qsvlite frequency --select {{column}} --limit {{5}} {{path/to/file.csv}}`

- Full-join two CSV files on a column from each (default is inner join):

`qsvlite join --full {{column1}} {{path/to/file1.csv}} {{column2}} {{path/to/file2.csv}}`
