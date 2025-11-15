# base64

> Encode or decode file or `stdin` to/from base64, to `stdout`.
> More information: <https://manned.org/base64>.

- Encode a file:

`base64 {{path/to/file}}`

- Wrap encoded output at a specific width (`0` disables wrapping):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{path/to/file}}`

- Decode a file:

`base64 {{[-d|--decode]}} {{path/to/file}}`

- Encode from `stdin`:

`{{command}} | base64`

- Decode from `stdin`:

`{{command}} | base64 {{[-d|--decode]}}`
