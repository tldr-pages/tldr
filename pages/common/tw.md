# tw

> Tabiew, a lightweight TUI application to view and query tabular data files.
> Supports CSV, TSV, Parquet, JSON, JSONL, Arrow, FWF, SQLite, Excel, and more.
> More information: <https://github.com/shshemi/tabiew>.

- Open one or more files, detecting the format based on the file extension:

`tw {{path/to/file1 path/to/file2 ...}}`

- Open a file, overriding the format detection:

`tw {{path/to/file}} {{[-f|--format]}} {{csv|tsv|parquet|sqlite|excel|...}}`

- Open a delimiter-separated file with a custom separator:

`tw {{path/to/file.csv}} --separator '{{|}}'`

- Open a delimiter-separated file without a header row:

`tw {{path/to/file.csv}} --no-header`

- Read tabular data from `stdin`:

`curl {{[-s|--silent]}} {{https://example.com/data.csv}} | tw`

- Open files with identical columns and concatenate them vertically into a single table:

`tw --multiparts {{path/to/part1.csv path/to/part2.csv ...}}`
