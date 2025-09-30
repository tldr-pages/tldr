# docker compose

> Run and manage multi container Docker applications.
> More information: <https://docs.docker.com/reference/cli/docker/compose/>.

- List all running containers:

`docker compose ps`

- Create and start all containers in the background using a `docker-compose.yml` file from the current directory:

`docker compose up {{[-d|--detach]}}`

- Start all containers, rebuild if necessary:

`docker compose up --build`

- Start all containers by specifying a project name and using an alternate compose file:

`docker compose {{[-p|--project-name]}} {{project_name}} {{[-f|--file]}} {{path/to/file}} up`

- Stop all running containers:

`docker compose stop`

- Stop and remove all containers, networks, images, and volumes:

`docker compose down --rmi all {{[-v|--volumes]}}`

- Follow logs for all containers:

`docker compose logs {{[-f|--follow]}}`

- Follow logs for a specific container:

`docker compose logs {{[-f|--follow]}} {{container_name}}`
