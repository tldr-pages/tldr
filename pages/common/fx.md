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

- Parse a TOML input file into JSON:

`fx --toml {{path/to/file.toml}}`

- Parse a YAML input file into JSON:

`fx --yaml {{path/to/file.yaml}}`
