# doctl databases

> Manage your MySQL, Redis, PostgreSQL, and MongoDB database services.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases>.

- Run a `doctl databases` command with an access token:

`doctl databases {{command}} --access-token {{access_token}}`

- Get details for a database cluster:

`doctl databases get`

- List your database clusters:

`doctl databases list`

- Create a database cluster:

`doctl databases create {{database_name}}`

- Delete a cluster:

`doctl databases delete {{database_id}}`
