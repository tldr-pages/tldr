# mariadb-binlog

> Utility for processing MariaDB binary log files.
> More information: <https://manned.org/mariadb-binlog>.

- Show events from a specific binary log file:

`mariadb-binlog {{path/to/binlog}}`

- Show entries from a binary log for a specific database:

`mariadb-binlog {{[-d|--database]}} {{database_name}} {{path/to/binlog}}`

- Show events from a binary log between specific dates:

`mariadb-binlog --start-datetime '{{2022-01-01 01:00:00}}' --stop-datetime '{{2022-02-01 01:00:00}}' {{path/to/binlog}}`

- Show events from a binary log between specific positions:

`mariadb-binlog {{[-j|--start-position]}} {{100}} --stop-position {{200}} {{path/to/binlog}}`

- Show binary log from a MariaDB server on the given host:

`mariadb-binlog {{[-h|--host]}} {{hostname}} {{path/to/binlog}}`
