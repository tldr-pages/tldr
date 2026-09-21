# csvlens

> Interactive viewer for CSV files in the terminal.
> More information: <https://github.com/YS-L/csvlens>.

- Open a file:

`csvlens {{path/to/file.csv}}`

- Open a file that uses a specific delimiter, or detect the delimiter automatically:

`csvlens {{[-d|--delimiter]}} {{;|auto}} {{path/to/file}}`

- Open a tab-separated file:

`csvlens {{[-t|--tab-separated]}} {{path/to/file.tsv}}`

- Treat the first row as data instead of as headers:

`csvlens --no-headers {{path/to/file.csv}}`

- Display only the columns whose names match a `regex`:

`csvlens --columns "{{column1|column2}}" {{path/to/file.csv}}`

- Display only the rows containing a cell that matches a `regex`:

`csvlens --filter "{{value1|value2}}" {{path/to/file.csv}}`

- Reload the file automatically when it changes on disk:

`csvlens --auto-reload {{path/to/file.csv}}`

- Display version:

`csvlens {{[-V|--version]}}`
