# json5

> Convert JSON5 files to JSON.
> More information: <https://json5.org/#cli>.

- Convert JSON5 `stdin` to JSON `stdout`:

`echo {{input}} | json5`

- Convert a JSON5 file to JSON and output to `stdout`:

`json5 {{path/to/input_file.json5}}`

- Convert a JSON5 file to the specified JSON file:

`json5 {{path/to/input_file.json5}} {{[-o|--out-file]}} {{path/to/output_file.json}}`

- Validate a JSON5 file:

`json5 {{path/to/input_file.json5}} {{[-v|--validate]}}`

- Specify the number of spaces to indent by (or "t" for tabs):

`json5 {{[-s|--space]}} {{indent_amount}}`

- Display help:

`json5 {{[-h|--help]}}`
