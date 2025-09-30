# base64

> Encode or decode file or `stdin` to/from base64, to `stdout` or another file.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Encode a file to `stdout`:

`base64 {{[-i|--input]}} {{path/to/file}}`

- Encode a file to the specified output file:

`base64 {{[-i|--input]}} {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- Wrap encoded output at a specific width (`0` disables wrapping):

`base64 {{[-b|--break]}} {{0|76|...}} {{path/to/file}}`

- Decode a file to `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{path/to/file}}`

- Encode from `stdin` to `stdout`:

`{{command}} | base64`

- Decode from `stdin` to `stdout`:

`{{command}} | base64 {{[-d|--decode]}}`
