# doctl databases user

> View details for, and create, database users.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/user>.

- Run a `doctl databases user` command with an access token:

`doctl {{[d|databases]}} {{[u|user]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Retrieve details about a database user:

`doctl {{[d|databases]}} {{[u|user]}} {{[g|get]}} {{database_id}} {{user_name}}`

- Retrieve a list of database users for a given database:

`doctl {{[d|databases]}} {{[u|user]}} {{[ls|list]}} {{database_id}}`

- Reset the auth password for a given user:

`doctl {{[d|databases]}} {{[u|user]}} {{[rs|reset]}} {{database id}} {{user_name}}`

- Reset the MySQL auth plugn for a given user:

`doctl {{[d|databases]}} {{[u|user]}} {{[rs|reset]}} {{database_id}} {{user_name}} {{caching_sha2_password|mysql_native_password}}`

- Create a user in the given database with a given username:

`doctl {{[d|databases]}} {{[u|user]}} {{[c|create]}} {{database_id}} {{user_name}}`

- Delete a user from the given database with the given username:

`doctl {{[d|databases]}} {{[u|user]}} {{[rm|delete]}} {{database_id}} {{user_name}}`
