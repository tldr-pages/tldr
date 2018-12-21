# pg_ctl

> Utility for controlling a PostgreSQL server and database cluster.

- Start a PostgreSQL server:

`pg_ctl -D {{data_directory}} -l {{log_file_name}}`

- Initialize a PostgreSQL database cluster:

`pg_ctl -D {{data_directory}} init`

- Stop a PostgreSQL server:

`pg_ctl -D {{data_directory}} stop`

- Restart a PostgreSQL server:

`pg_ctl -D {{data_directory}} restart`
