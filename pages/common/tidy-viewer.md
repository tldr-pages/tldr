# tidy-viewer

> A data pretty-printer with column styling for CSV, TSV, PSV, Parquet, and Arrow IPC files.
> Commonly aliased as `tv`.
> More information: <https://github.com/alexhallam/tv>.

- Pretty-print a CSV file:

`tidy-viewer {{path/to/file.csv}}`

- Pretty-print data piped from `stdin`:

`cat {{path/to/file.csv}} | tidy-viewer`

- Pretty-print a file with a custom [s]eparator (e.g. a pipe-separated file):

`tidy-viewer {{[-s|--delimiter]}} '|' {{path/to/file.psv}}`

- Display data with a specific [c]olor palette (1: nord, 2: one_dark, 3: gruvbox, 4: dracula, 5: solarized light):

`tidy-viewer {{[-c|--color]}} {{3}} {{path/to/file.csv}}`

- Print all rows instead of the first 25, paging through the output:

`tidy-viewer {{[-f|--force-all-rows]}} {{path/to/file.csv}} | less -S`

- Display help:

`tidy-viewer {{[-h|--help]}}`

- Display version:

`tidy-viewer {{[-V|--version]}}`
