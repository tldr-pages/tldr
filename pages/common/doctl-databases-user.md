# doctl databases user

> View details for, and create, database users.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/user>.

- Run a `doctl databases user` command with an access token:

`doctl databases user {{command}} --access-token {{access_token}}`

- Retrieve details about a database user:

`doctl databases user get {{database_id}} {{user_name}}`

- Retrieve a list of database users for a given database:

`doctl databases user list {{database_id}}`

- Reset the auth password for a given user:

`doctl databases user reset {{database id}} {{user_name}}`

- Reset the MySQL auth plugn for a given user:

`doctl databases user reset {{database_id}} {{user_name}} {{caching_sha2_password|mysql_native_password}}`

- Create a user in the given database with a given username:

`doctl databases user create {{database_id}} {{user_name}}`

- Delete a user from the given database with the given username:

`doctl databases user delete {{database_id}} {{user_name}}`
