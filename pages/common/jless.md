# jless

> An interactive JSON viewer.
> More information: <https://jless.io/user-guide>.

- View a JSON file:

`jless {{path/to/file.json}}`

- View JSON from `stdin`:

`{{cat path/to/file.json}} | jless`

- View a YAML file (`--yaml` is optional, the format is automatically detected from the file extension):

`jless --yaml {{path/to/file.yaml}}`

- View JSON in line mode (quote object keys and include curly and square brackets):

`jless {{path/to/file.jsonl}} {{[-m|--mode]}} line`
