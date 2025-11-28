# qrcp

> A file transfer tool.
> More information: <https://github.com/claudiodangelis/qrcp#usage>.

- Send a file or directories:

`qrcp send {{path/to/file_or_directory1 path/to/file_directory2 ...}}`

- Receive files:

`qrcp receive`

- Compress content before transferring:

`qrcp send --zip {{path/to/file_or_directory}}`

- Use a specific port:

`qrcp {{send|receive}} {{[-p|--port]}} {{port_number}}`

- Use a specific network interface:

`qrcp {{send|receive}} {{[-i|--interface]}} {{interface}}`

- Keep the server alive:

`qrcp {{send|receive}} --keep-alive`
