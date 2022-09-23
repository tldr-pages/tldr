# qrcp

> A file transfer tool.
> More information: <https://github.com/claudiodangelis/qrcp>.

- Send a file(s) or directories:

`qrcp send {{path/to/file_or_directory}}`

- Receive file(s):

`qrcp receive`

- [z]ip content before transferring:

`qrcp send --zip {{path/to/file_or_directory}}`

- Specify [p]ort to use for the server:

`qrcp send/receive --port port`

- Specify the network [i]nterface to use:

`qrcp send/receive --interface interface`

- Keep the server alive:

`qrcp send/receive --keep-alive`
