# jless

> Command-line JSON viewer for reading, exploring, and searching JSON data.
> Supports newline-delimited JSON and vim-inspired commands.
> More information: <https://jless.io/user-guide>.

- Open a JSON file:

`jless {{path/to/file.json}}`

- View JSON from `stdin`:

`{{cat path/to/file.json}} | jless`

- View JSON returned by a URL:

`curl {{url}} | jless`

- View newline-delimited JSON logs:

`jless {{path/to/file.jsonl}}`

- View YAML data:

`jless --yaml {{path/to/file.yaml}}`
