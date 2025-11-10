# col

> Filter reverse line feeds from input.
> More information: <https://manned.org/col>.

- Filter reverse line feeds and output with spaces instead of tabs:

- Filter reverse line feeds from input:

`{{command}} | col`

`{{command}} | col {{[-x|--spaces]}}`

- Remove backspaces, output only the last character written to each position:

`{{command}} | col {{[-b|--no-backspaces]}}`

- Specify a buffer size with a specific number of lines:

`{{command}} | col -l {{num}}`

- Format a manual page for viewing with `less`:

`man ls | col {{[-b|--no-backspaces]}} | less`

- Process a file with reverse line feeds and save the cleaned output:

`cat {{path/to/input_file}} | col -x > {{output_file}}`
