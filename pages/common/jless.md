# jless

> An interactive JSON viewer.
> More information: <https://jless.io/user-guide>.

- View a JSON file:

`jless {{path/to/file.json}}`

- View JSON from `stdin`:

`{{cat path/to/file.json}} | jless`

- View a YAML file:

`jless --yaml {{path/to/file.yaml}}`

- View JSON in line mode (newline-delimited data):

`jless {{path/to/file.jsonl}} {{[-m|--mode]}} line`
