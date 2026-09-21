# vd

> Interactive multitool for tabular data.
> More information: <https://www.visidata.org/docs/>.

- Open one or more files in the interactive interface:

`vd {{path/to/file1 path/to/file2 ...}}`

- Open a file, specifying the format instead of detecting it from the file extension:

`vd {{[-f|--filetype]}} {{csv|json|sqlite|xlsx|...}} {{path/to/file}}`

- Read tabular data from `stdin`:

`{{command}} | vd`

- Convert a file to a different format without opening the interface:

`vd {{[-b|--batch]}} {{path/to/input.csv}} {{[-o|--output]}} {{path/to/output.json}}`

- Replay a saved command log against a file:

`vd {{[-p|--play]}} {{path/to/commands.vdj}} {{path/to/file}}`

- Display version:

`vd --version`
