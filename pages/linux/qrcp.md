# qrcp

> A file transfer tool.
> More information: <https://github.com/claudiodangelis/qrcp>.

- Send a file or directories:

`qrcp send {{path/to/file_or_directory path/to/file_directory ...}}`

- Receive files:

`qrcp receive`

- Compress content before transferring:

`qrcp send --zip {{path/to/file_or_directory}}`

- Use a specific [p]ort:

`qrcp {{send|receive}} --port {{port_number}}`

- Use a specific network [i]nterface:

`qrcp {{send|receive}} --interface interface`

- Keep the server alive:

`qrcp {{send|receive}} --keep-alive`
