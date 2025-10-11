# fx

> Terminal JSON viewer and processor.
> More information: <https://github.com/antonmedv/fx>.

- View a JSON file interactively:

`fx file.json`

- Pretty-print and colorize JSON from stdin:

`cat file.json | fx`

- Open JSON data from a URL:

`curl https://dummyjson.com/products | fx`

- Filter JSON using JavaScript-like expressions:

`fx file.json .name`

- Parse input as TOML to JSON:

`fx --toml Cargo.toml`

- Parse input as YAML to JSON:

`fx --yaml pipeline.yaml`
