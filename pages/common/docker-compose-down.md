# docker compose down

> Stop and remove containers, networks, images, and volumes created by docker-compose up.
> More information: <https://docs.docker.com/reference/cli/docker/compose/down/>.
- Stop and remove all containers and networks:

`docker compose down`

- Stop and remove containers, networks, and all images used by services:

`docker compose down --rmi all`

- Stop and remove containers, networks, and only images without a custom tag:

`docker compose down --rmi local`

- Stop and remove containers, networks, and all volumes:

`docker compose down {{[-v|--volumes]}}`

- Stop and remove everything including orphaned containers:

`docker compose down --remove-orphans`

- Stop and remove containers using an alternate compose file:

`docker compose {{[-f|--file]}} {{path/to/file.yml}} down`

- Stop and remove containers with a custom timeout in seconds:

`docker compose down {{[-t|--timeout]}} {{timeout}}`

- Remove containers for services not defined in the Compose file:

`docker compose down --remove-orphans {{[-v|--volumes]}}`