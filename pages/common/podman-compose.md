# podman-compose

> Run and manage compose spec container definition.
> More information: <https://github.com/containers/podman-compose>.

- List all running containers:

`podman-compose ps`

- Create and start all containers in the background using a local `docker-compose.yml`:

`podman-compose up -d`

- Start all containers, building if needed:

`podman-compose up --build`

- Start all containers using an alternate compose file:

`podman-compose {{path/to/file}} up`

- Stop all running containers:

`podman-compose stop`

- Remove all containers, networks, and volumes:

`podman-compose down --volumes`

- Follow logs for a containers (omit container name for all):

`podman-compose logs --follow {{container_name}}`

- Run a one-time command in a service (no ports are mapped):

`podman-compose run {{service_name}} {{command}}`
