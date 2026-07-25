# docker compose stop

> Stop running containers without removing them.
> More information: <https://docs.docker.com/reference/cli/docker/compose/stop>.

- Stop all running services:

`docker compose stop`

- Stop specific services:

`docker compose stop {{service_1 service_2 ...}}`

- Stop with a custom shutdown timeout in seconds:

`docker compose stop {{[-t|--timeout]}} {{seconds}}`

- Stop services defined in a specific compose file:

`docker compose {{[-f|--file]}} {{path/to/compose_file}} stop`

- Dry run (show operations without executing):

`docker compose stop --dry-run`

- Stop specific services with a custom timeout:

`docker compose stop {{[-t|--timeout]}} {{seconds}} {{service_1 service_2 ...}}`
