# pg_createsubscriber

> Convert a physical replica into a new logical replica.
> More information: <https://www.postgresql.org/docs/current/app-pgcreatesubscriber.html>.

- Convert a physical replica to a logical replica for a specific database:

`pg_createsubscriber {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Perform a dry run without modifying the target directory:

`pg_createsubscriber {{[-n|--dry-run]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Enable two-phase commit for the subscription:

`pg_createsubscriber {{[-T|--enable-two-phase]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Convert with verbose output:

`pg_createsubscriber {{[-v|--verbose]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Display help:

`pg_createsubscriber {{[-?|--help]}}`
