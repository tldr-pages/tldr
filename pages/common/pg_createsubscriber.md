# pg_createsubscriber

> Convert a physical replica into a new logical replica.
> More information: <https://www.postgresql.org/docs/current/app-pgcreatesubscriber.html>.

- Convert a physical replica to a logical replica for a specific database:

`pg_createsubscriber {{[-d|--database]}} {{database_name}} {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-P|--publisher-server]}} {{connection_string}}`

- Perform a dry run without modifying the target directory:

`pg_createsubscriber {{[-d|--database]}} {{database_name}} {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-P|--publisher-server]}} {{connection_string}} {{[-n|--dry-run]}}`

- Enable two-phase commit for the subscription:

`pg_createsubscriber {{[-d|--database]}} {{database_name}} {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-P|--publisher-server]}} {{connection_string}} {{[-T|--enable-two-phase]}}`

- Convert with verbose output:

`pg_createsubscriber {{[-d|--database]}} {{database_name}} {{[-D|--pgdata]}} {{path/to/data_directory}} {{[-P|--publisher-server]}} {{connection_string}} {{[-v|--verbose]}}`

- Display help:

`pg_createsubscriber {{[-?|--help]}}`
