# rev

> Reverse a line of text or a file.
> More information: <https://manned.org/rev>.

- Reverse text typed into terminal:

`rev`

- Reverse the text string "hello":

`echo "hello" | rev`

- Reverse an entire file and print to `stdout`:

`rev {{path/to/file}}`

- Use '\0' as a line separator (zero termination):

`rev {{[-0|--zero]}} {{path/to/file}}`

- Display help:

`rev {{[-h|--help]}}`

- Display version:

`rev {{[-V|--version]}}`
