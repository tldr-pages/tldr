# foreman

> Manage Procfile-based application.

- Start an application:

`foreman start {{process}}`

- Run one-off commands with the process's environment:

`foreman run {{command}}`

- Start all processes except the one named worker:

`foreman start -m all=1,worker=0`
