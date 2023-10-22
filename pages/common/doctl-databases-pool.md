# doctl databases pool

> Manage connection pools for your database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- Run a `doctl databases pool` command with an access token:

`doctl databases pool {{command}} --access-token {{access_token}}`

- Retrieve information about a database connection pool:

`doctl databases pool get {{database_id}} {{pool_name}}`

- List connection pools for a database cluster:

`doctl databases pool list {{database_id}}`

- Create a connection pool for a database:

`doctl databases pool create {{database_id}} {{pool_name}} --db {{new_pool_name}} --size {{pool_size}}`

- Delete a connection pool for a database:

`doctl databases pool create {{database_id}} {{pool_name}}`
