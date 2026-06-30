# tidy-viewer

> A data pretty-printer with column styling for CSV, TSV, PSV, Parquet, and Arrow IPC files.
> Commonly aliased as `tv`.
> More information: <https://github.com/alexhallam/tv#help>.

- Pretty-print the first 25 rows of a CSV file:

`tidy-viewer {{path/to/file.csv}}`

- Pretty-print data piped from `stdin`:

`cat {{path/to/file.csv}} | tidy-viewer`

- Pretty-print a file with a custom [s]eparator (e.g. a pipe):

`tidy-viewer {{[-s|--delimiter]}} '|' {{path/to/file.psv}}`

- Display data with a specific color palette (1: nord, 2: one_dark, 3: gruvbox, 4: dracula, 5: solarized light):

`tidy-viewer {{[-c|--color]}} {{3}} {{path/to/file.csv}}`

- Print all rows in color, paging through the output:

`tidy-viewer {{[-af|--color-always --force-all-rows]}} {{path/to/file.csv}} | less -RS`

- Display help:

`tidy-viewer {{[-h|--help]}}`

- Display version:

`tidy-viewer {{[-V|--version]}}`
