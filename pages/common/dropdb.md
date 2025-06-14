# dropdb

> Remove a PostgreSQL database.
> This is a simple wrapper around the SQL command `DROP DATABASE`.
> More information: <https://www.postgresql.org/docs/current/app-dropdb.html>.

- Destroy a database:

`dropdb {{dbname}}`

- Request a verification prompt before any destructive actions:

`dropdb --interactive {{database_name}}`

- Connect with a specific username and destroy a database:

`dropdb --username={{username}} {{dbname}}`

- Force a password prompt before connecting to the database:

`dropdb --password {{dbname}}}}`

- Specify the server host name:

`dropdb --host={{host}} {{dbname}}`

- Specify the server port:

`dropdb --port={{port}} {{dbname}}`

- Attempt to terminate existing connections before destroying the database:

`dropdb --force {{dbname}}`
