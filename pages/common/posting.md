# posting

> A terminal-based HTTP API client (TUI), similar to Postman or Insomnia.
> Requests are stored as local YAML files and can be version controlled.
> More information: <https://posting.sh>.

- Start the interactive TUI:

`posting`

- Open a specific request collection directory:

`posting --collection {{path/to/collection/}}`

- Load environment variables from a file:

`posting --env {{path/to/.env}}`

- Open a collection with a specific environment file:

`posting --collection {{path/to/collection/}} --env {{path/to/.env}}`

- Start with a specific theme:

`posting --theme {{monokai}}`
