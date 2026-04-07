# jless

> A command-line JSON viewer with vim-inspired keybindings.
> Supports JSON and YAML files with syntax highlighting and interactive navigation.
> More information: <https://jless.io>.

- View a JSON file interactively:

`jless {{path/to/file.json}}`

- Read JSON from `stdin`:

`{{cat path/to/file.json}} | jless`

- View a YAML file:

`jless --yaml {{path/to/file.yaml}}`

- Expand or collapse the currently focused node:

`<Space>`

- Search forward for a pattern:

`/{{pattern}}`

- Copy the path to the currently focused node to the clipboard:

`yp`

- Copy the value of the currently focused node (pretty printed) to the clipboard:

`yy`

- Display help:

`<F1>`
