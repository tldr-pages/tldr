# transfersh

> An unofficial command-line client for transfer.sh.
> More information: <https://github.com/AlpixTM/transfersh>.

- Upload a file to transfer.sh:

`transfersh {{path/to/file}}`

- Upload a file showing a progress bar (requires Python package `requests_toolbelt`):

`transfersh --progress {{path/to/file}}`

- Upload a file using a different file name:

`transfersh --name {{filename}} {{path/to/file}}`

- Upload a file to a custom transfer.sh server:

`transfersh --servername {{upload.server.name}} {{path/to/file}}`

- Upload all files from a directory recursively:

`transfersh --recursive {{path/to/directory/}}`

- Upload a specific directory as an uncompressed tar:

`transfersh -rt {{path/to/directory}}`
