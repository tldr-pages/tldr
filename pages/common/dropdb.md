# dropdb

> Remove a PostgreSQL database.
> A simple wrapper around the SQL command `DROP DATABASE`.
> More information: <https://www.postgresql.org/docs/current/app-dropdb.html>.

- Destroy a database:

`dropdb {{database_name}}`

- Request a verification prompt before any destructive actions:

`dropdb {{database_name}} {{[-i|--interactive]}}`

- Connect with a specific username and destroy a database:

`dropdb {{database_name}} {{[-U|--username]}} {{username}}`

- Force a password prompt before connecting to the database:

`dropdb {{database_name}} {{[-W|--password]}}`

- Suppress a password prompt before connecting to the database:

`dropdb {{database_name}} {{[-w|--no-password]}}`

- Specify the server host name:

`dropdb {{database_name}} {{[-h|--host]}} {{host}}`

- Specify the server port:

`dropdb {{database_name}} {{[-p|--port]}} {{port}}`

- Attempt to terminate existing connections before destroying the database:

`dropdb {{database_name}} {{[-f|--force]}}`
