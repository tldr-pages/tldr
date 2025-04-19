# podman-compose

> Run and manage Compose Specification container definition.
> More information: <https://github.com/containers/podman-compose>.

- List all running containers:

`podman-compose ps`

- Create and start all containers in the background using a local `docker-compose.yml`:

`podman-compose up {{[-d|--detach]}}`

- Start all containers, building if needed:

`podman-compose up --build`

- Start all containers using an alternate compose file:

`podman-compose {{[-f|--file]}} {{path/to/file.yaml}} up`

- Stop all running containers:

`podman-compose stop`

- Remove all containers, networks, and volumes:

`podman-compose down {{[-v|--volumes]}}`

- Follow logs for a container (omit all container names):

`podman-compose logs {{[-f|--follow]}} {{container_name}}`

- Run a one-time command in a service with no ports mapped:

`podman-compose run {{service_name}} {{command}}`
