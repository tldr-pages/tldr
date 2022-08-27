# keep-header

> Keep first line untouched by a command, passing it directly to stdout
> More information: <https://github.com/eBay/tsv-utils#keep-header>.

- Sort a file and keep the first line at the top

`keep-header {{path/to/file}} -- sort`

- Output first line directly to stdout, pass rest through command:

`keep-header {{path/to/file}} -- {{command}}`

- Read from stdin, sorting all except the first line:

`cat {{path/to/file}} | keep-header -- {{command}}`

- Grep a file, keeping the first line whether it matches or not:

`keep-header {{path/to/file}} -- grep {{pattern}}`
