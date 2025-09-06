# doctl databases pool

> Manage connection pools for your database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- Run a `doctl databases pool` command with an access token:

`doctl {{[d|databases]}} {{[p|pool]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Retrieve information about a database connection pool:

`doctl {{[d|databases]}} {{[p|pool]}} {{[g|get]}} {{database_id}} {{pool_name}}`

- List connection pools for a database cluster:

`doctl {{[d|databases]}} {{[p|pool]}} {{[ls|list]}} {{database_id}}`

- Create a connection pool for a database:

`doctl {{[d|databases]}} {{[p|pool]}} {{[c|create]}} {{database_id}} {{pool_name}} --db {{new_pool_name}} --size {{pool_size}}`

- Delete a connection pool for a database:

`doctl {{[d|databases]}} {{[p|pool]}} {{[c|create]}} {{database_id}} {{pool_name}}`
