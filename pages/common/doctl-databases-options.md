# doctl databases options

> Enable the navigation of available options under each database engine.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/options>.

- Run a `doctl databases options` command with an access token:

`doctl {{[d|databases]}} {{[o|options]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Retrieve a list of the available database engines:

`doctl {{[d|databases]}} {{[o|options]}} {{[eng|engines]}}`

- Retrieve a list of the available regions for a given database engine:

`doctl {{[d|databases]}} {{[o|options]}} {{[r|regions]}} --engine {{pg|mysql|redis|mongodb}}`

- Retrieve a list of the available slugs for a given database engine:

`doctl {{[d|databases]}} {{[o|options]}} {{[s|slugs]}} --engine {{pg|mysql|redis|mongodb}}`

- Retrieve a list of the available versions for a given database engine:

`doctl {{[d|databases]}} {{[o|options]}} {{[v|versions]}} --engine {{pg|mysql|redis|mongodb}}`
