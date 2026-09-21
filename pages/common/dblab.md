# dblab

> Interactive TUI database client.
> Supports PostgreSQL, MySQL, SQLite3, Oracle, and SQL Server.
> More information: <https://dblab.app/>.

- Connect to a database using a connection URL:

`dblab {{[-u|--url]}} "{{postgres://user:password@localhost:5432/database}}"`

- Connect by passing the parameters individually:

`dblab --driver {{postgres}} --host {{localhost}} --port {{5432}} --user {{user}} --pass {{password}} --db {{database}}`

- Get the connection details from a configuration file:

`dblab --config`

- Pick from the previously saved connection profiles:

`dblab connect`

- Save the connection as a named profile to reuse later:

`dblab {{[-u|--url]}} "{{connection_url}}" --save-as {{profile_name}}`

- Force a read-only connection:

`dblab {{[-u|--url]}} "{{connection_url}}" --readonly`

- Limit the number of rows fetched for the table contents:

`dblab {{[-u|--url]}} "{{connection_url}}" --limit {{50}}`

- Display version:

`dblab {{[-v|--version]}}`
