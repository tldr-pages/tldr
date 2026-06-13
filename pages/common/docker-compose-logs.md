# docker compose logs

> View output from containers in a Docker Compose application.
> More information: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- View logs for all services:

`docker compose logs`

- View logs for a specific service:

`docker compose logs {{service_name}}`

- View logs and follow new output (like `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- View logs with timestamps:

`docker compose logs {{[-t|--timestamps]}}`

- View only the last `n` lines of logs for each container:

`docker compose logs {{[-n|--tail]}} {{n}}`

- View logs from a specific time onwards:

`docker compose logs --since {{timestamp}}`

- View logs until a specific time:

`docker compose logs --until {{timestamp}}`

- View logs for multiple specific services:

`docker compose logs {{service1 service2 ...}}`
