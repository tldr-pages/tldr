# keep-header

> Convenience utility that runs Unix commands in a header-aware fashion.
> More information: <https://github.com/eBay/tsv-utils#keep-header>.

- Pass all but the first line to command and keep the first line:

`keep-header {{path/to/file}} -- {{command}}`

- Sort files except for retaining a single header line:

`keep-header {{path/to/file}} -- sort`

- Read from stdin, sorting all except the first line:

`cat {{path/to/file}} | keep-header -- sort`

- Grep a file, keeping the header line:

`keep-header {{path/to/file}} -- grep {{pattern}}`
