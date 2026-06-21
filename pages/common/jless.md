# jless

> Interactively view, explore, and search JSON and YAML data.
> More information: <https://jless.io/user-guide>.

- View a JSON file:

`jless {{path/to/file.json}}`

- Read JSON from `stdin`:

`{{command}} | jless`

- View a YAML file:

`jless --yaml {{path/to/file.yaml}}`

- Start in line mode, showing closing delimiters, commas, and quoted object keys:

`jless {{[-m|--mode]}} line {{path/to/file.json}}`

- [Interactive] Expand or collapse the focused object or array:

`<Space>`

- [Interactive] Search forward for a `regex` (press `<n>`/`<N>` to go to the next/previous match):

`</>{{search_pattern}}<Enter>`
