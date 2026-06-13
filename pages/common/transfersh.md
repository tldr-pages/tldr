# transfersh

> An unofficial client for transfer.sh.
> More information: <https://github.com/AlpixTM/transfersh>.

- Upload a file to transfer.sh:

`transfersh {{path/to/file}}`

- Upload a file showing a progress bar (requires Python package `requests_toolbelt`):

`transfersh {{[-p|--progress]}} {{path/to/file}}`

- Upload a file using a different file name:

`transfersh {{[-n|--name]}} {{filename}} {{path/to/file}}`

- Upload a file to a custom transfer.sh server:

`transfersh {{[-sn|--servername]}} {{upload.server.name}} {{path/to/file}}`

- Upload all files from a directory recursively:

`transfersh {{[-r|--recursive]}} {{path/to/directory}}/`

- Upload a specific directory as an uncompressed tar:

`transfersh {{[-rt|--recursive --tar]}} {{path/to/directory}}`
