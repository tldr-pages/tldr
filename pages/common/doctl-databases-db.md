# doctl databases db

> Manage databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/db>.

- Run a `doctl databases db` command with an access token:

`doctl databases db {{command}} --access-token {{access_token}}`

- Retrieve the name of the given database hosted in the given database cluster:

`doctl databases db get {{database_id}} {{database_name}}`

- List existing databases hosted within a given database cluster:

`doctl databases db list {{database_id}}`

- Create a database with the given name in the given database cluster:

`doctl databases db create {{database_id}} {{database_name}}`

- Delete the database with the given name in the given database cluster:

`doctl databases db delete {{database_id}} {{database_name}}`
