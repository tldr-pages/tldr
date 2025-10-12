# fx

> View and process JSON.
> More information: <https://fx.wtf/getting-started>.

- View a JSON file interactively:

`fx {{path/to/file.json}}`

- Pretty-print and colorize JSON from `stdin`:

`cat {{path/to/file.json}} | fx`

- Open JSON data from a URL:

`curl {{url}} | fx`

- Filter JSON using JavaScript-like expressions:

`fx {{path/to/file.json}} {{.name}}`

- Parse input as TOML to JSON:

`fx --toml {{path/to/file.toml}}`

- Parse input as YAML to JSON:

`fx --yaml {{path/to/file.yaml}}`
