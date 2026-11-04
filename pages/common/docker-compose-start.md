# docker compose start

> Start existing containers for services.
> More information: <https://docs.docker.com/reference/cli/docker/compose/start/>.

- Start existing containers for all services:

`docker compose start`

- Start existing containers for one or more services:

`docker compose start {{service1 service2 ...}}`

- Simulate starting existing containers:

`docker compose start --dry-run`

- Start existing containers and wait for services to be running or healthy:

`docker compose start --wait`

- Start existing containers and wait up to a specified number of seconds:

`docker compose start --wait --wait-timeout {{seconds}}`
