# pg_ctl

> Utility for controlling a PostgreSQL server and database cluster.
> More information: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- Initialize a new PostgreSQL database cluster:

`pg_ctl init {{[-D|--pgdata]}} {{path/to/data_directory}}`

- Start a PostgreSQL server:

`pg_ctl start {{[-D|--pgdata]}} {{path/to/data_directory}}`

- Stop a PostgreSQL server:

`pg_ctl stop {{[-D|--pgdata]}} {{path/to/data_directory}}`

- Restart a PostgreSQL server:

`pg_ctl restart {{[-D|--pgdata]}} {{path/to/data_directory}}`

- Reload the PostgreSQL server configuration:

`pg_ctl reload {{[-D|--pgdata]}} {{path/to/data_directory}}`
