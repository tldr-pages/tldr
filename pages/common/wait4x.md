# wait4x

> Wait for a port or service to enter a requested state, with support for TCP, HTTP, DNS, databases, and message queues.
> Some subcommands such as `tcp` and `http` have their own usage documentation.
> More information: <https://github.com/wait4x/wait4x>.

- Wait for a TCP port to become available:

`wait4x tcp {{localhost:8080}}`

- Wait for an HTTP endpoint to return a specific status code:

`wait4x http {{https://example.com/health}} --expect-status-code {{200}}`

- Wait for a PostgreSQL database to become ready:

`wait4x postgresql '{{postgres://user:password@localhost:5432/mydb?sslmode=disable}}'`

- Wait for a Redis server to become available:

`wait4x redis {{redis://localhost:6379}}`

- Wait for a service with a custom timeout and check interval:

`wait4x tcp {{localhost:3306}} --timeout {{30s}} --interval {{2s}}`

- Wait for multiple services in parallel:

`wait4x tcp {{localhost:3306}} {{localhost:6379}} {{localhost:27017}}`

- Display help for a subcommand:

`wait4x {{subcommand}} --help`

- Display version:

`wait4x version`
