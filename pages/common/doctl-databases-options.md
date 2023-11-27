# doctl databases options

> Enable the navigation of available options under each database engine.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/options>.

- Run a `doctl databases options` command with an access token:

`doctl databases options {{command}} --access-token {{access_token}}`

- Retrieve a list of the available database engines:

`doctl databases options engines`

- Retrieve a list of the available regions for a given database engine:

`doctl databases options regions --engine {{pg|mysql|redis|mongodb}}`

- Retrieve a list of the available slugs for a given database engine:

`doctl databases options slugs --engine {{pg|mysql|redis|mongodb}}`

- Retrieve a list of the available versions for a given database engine:

`doctl databases options versions --engine {{pg|mysql|redis|mongodb}}`
