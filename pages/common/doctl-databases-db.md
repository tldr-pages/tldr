# doctl databases db

> Manage databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/db>.

- Run a `doctl databases db` command with an access token:

`doctl {{[d|databases]}} db {{command}} {{[-t|--access-token]}} {{access_token}}`

- Retrieve the name of the given database hosted in the given database cluster:

`doctl {{[d|databases]}} db {{[g|get]}} {{database_id}} {{database_name}}`

- List existing databases hosted within a given database cluster:

`doctl {{[d|databases]}} db {{[ls|list]}} {{database_id}}`

- Create a database with the given name in the given database cluster:

`doctl {{[d|databases]}} db {{[c|create]}} {{database_id}} {{database_name}}`

- Delete the database with the given name in the given database cluster:

`doctl {{[d|databases]}} db {{[rm|delete]}} {{database_id}} {{database_name}}`
