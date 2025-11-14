# jless

> A command-line JSON viewer designed for reading, exploring and searching through JSON data.
> More information: <https://jless.io>.

- View a JSON file:

`jless {{path/to/file.json}}`

- View JSON from `stdin`:

`{{command}} | jless`

- View a JSON file with line numbers:

`jless {{[-n|--line-numbers]}} {{path/to/file.json}}`

- View JSON and start in search mode:

`jless {{[-s|--search]}} {{search_term}} {{path/to/file.json}}`

- View JSON with a specific tab width:

`jless {{[-t|--tab-width]}} {{4}} {{path/to/file.json}}`

- View JSON without syntax highlighting:

`jless {{[--no-highlight]}} {{path/to/file.json}}`

- View JSON and expand all arrays and objects by default:

`jless {{[-e|--expand-all]}} {{path/to/file.json}}`

- Display help:

`jless {{[-h|--help]}}`