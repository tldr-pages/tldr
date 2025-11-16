# ttyd

> Share a terminal or any command over the web.
> More information: <https://github.com/tsl0922/ttyd#command-line-options>.

- Start a web server sharing the `bash` shell on the default port (7681):

`ttyd bash`

- Start `bash` on a specific port:

`ttyd bash {{[-p|--port]}} {{8080}}`

- Allow clients to write to the terminal:

`ttyd {{command}} {{[-W|--writable]}}`

- Enable a client option, like ZMODEM file transfers:

`ttyd {{command}} {{[-t|--client-option]}} {{option=value}}`

- Display help:

`ttyd {{[-h|--help]}}`

- Display version:

`ttyd {{[-v|--version]}}`
