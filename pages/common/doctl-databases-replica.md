# doctl databases replica

> Manage specific databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/replica/>.

- Run a doctl databases replica command with an access token:

`doctl databases pool [command] --access-token {{ access_token }}`

- Retrieve information about a read-only database replica:

`doctl databases replica get {{ database id }} {{ replica name }}`

- Retrieve list of read-only database replicas:

`doctl databases replica list {{ database id }}`

- Create a read-only database replica:

`doctl databases replica create {{ database id }} {{ replica name }}`

- Delete a read-only database replica:

`doctl databases replica delete {{ database id }} {{ replica name }}`