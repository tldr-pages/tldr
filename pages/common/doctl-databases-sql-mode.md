# doctl databases sql-mode

> View and configure a MySQL database cluster's global SQL modes.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/sql-mode/>.

- Run a `doctl databases sql-mode` command with an access token:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Get a MySQL database cluster's SQL modes:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{[g|get]}} {{database_id}}`

- Overwrite a MySQL database cluster's SQL modes to the specified modes:

`doctl {{[d|databases]}} {{[sm|sql-mode]}} {{[s|set]}} {{database_id}} {{sql_mode_1 sql_mode_2 ...}}`
