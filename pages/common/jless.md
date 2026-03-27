# jless

> A command-line JSON viewer designed for reading, exploring, and searching through JSON data.
> More information: <https://jless.io>.

- View a JSON file:

`jless {{path/to/file.json}}`

- View JSON from `stdin`:

`{{cat path/to/file.json}} | jless`

- View a YAML file:

`jless --yaml {{path/to/file.yaml}}`

- View JSON in line mode (newline-delimited data):

`jless --line-mode {{path/to/file.jsonl}}`

- View JSON with initial search query:

`jless --search {{query}} {{path/to/file.json}}`
