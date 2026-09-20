# base64

> Encode or decode file or `stdin` to/from base64, to `stdout`.
> More information: <https://man.freebsd.org/cgi/man.cgi?base64>.

- Encode a file to `stdout`:

`base64 {{path/to/file}}`

- Wrap encoded output at a specific column width (`0` disables wrapping):

`base64 -w {{0|76|...}} {{path/to/file}}`

- Decode a file to `stdout`:

`base64 -d {{path/to/file}}`

- Encode from `stdin` to `stdout`:

`{{command}} | base64`

- Decode from `stdin` to `stdout`:

`{{command}} | base64 -d`
