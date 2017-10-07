# foreman

> Manage Procfile-based application.

- Start an application with Procfile in current directory:

`foreman start`

- Start a specific application:

`foreman start {{process}}`

- Validate Procfile format:

`foreman check`

- Run one-off commands with the process's environment:

`foreman run {{command}}`

- Start all processes except the one named worker:

`foreman start -m all=1,worker=0`
