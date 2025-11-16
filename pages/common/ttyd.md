# ttyd

> Share a terminal or any command over the web.
> More information: <https://github.com/tsl0922/ttyd#command-line-options>.

- Start a web server sharing the `bash` shell on the default port (7681):

`ttyd bash`

- Start `bash` on a specific port:

`ttyd {{[-p|--port]}} {{8080}} bash`

- Allow clients to write to the terminal:

`ttyd {{[-W|--writable]}} {{command}}`

- Set client options:

`ttyd {{[-t|--client-option]}} {{key=value}} {{command}}`

- Display help:

`ttyd {{[-h|--help]}}`

- Display version:

`ttyd {{[-v|--version]}}`
