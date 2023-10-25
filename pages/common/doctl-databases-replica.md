# doctl databases replica

> Manage read-only replicas associated with a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- Run a `doctl databases replica` command with an access token:

`doctl databases pool {{command}} --access-token {{access_token}}`

- Retrieve information about a read-only database replica:

`doctl databases replica get {{database_id}} {{replica_name}}`

- Retrieve list of read-only database replicas:

`doctl databases replica list {{database_id}}`

- Create a read-only database replica:

`doctl databases replica create {{database_id}} {{replica_name}}`

- Delete a read-only database replica:

`doctl databases replica delete {{database_id}} {{replica_name}}`
