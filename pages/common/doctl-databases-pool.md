# doctl databases pool

> Manage specific databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/pool/>.

- Run a doctl databases maintenance-window command with an access token:

`doctl databases pool [command] --access-token {{ access_token }}`

- Retrieve information about a database connection pool:

`doctl databases pool get {{ database id }} {{ pool name }}`

- List connection pools for a database cluster:

`doctl databases pool list {{ database id }}`

- Create a connection pool for a database:

`doctl databases pool create {{ database id }} {{ pool name }} --db {{ new pool name }} --size {{ pool size }}`

- Delete a connection pool for a database:

`doctl databases pool create {{ database id }} {{ pool name }}`