# docker

> Manage Docker containers and images.
> Some subcommands such as `run` have their own usage documentation.
> More information: <https://docs.docker.com/reference/cli/docker/>.

- List all Docker containers (running and stopped):

`docker ps {{[-a|--all]}}`

- Start a container from an image, with a custom name:

`docker run --name {{container_name}} {{image}}`

- Start or stop an existing container:

`docker {{start|stop}} {{container_name}}`

- Pull an image from a Docker registry:

`docker pull {{image}}`

- Display the list of already downloaded images:

`docker images`

- Open an interactive shell inside a running container:

`docker exec {{[-it|--interactive --tty]}} {{container_name}} {{bash|sh}}`

- Remove stopped containers:

`docker rm {{container1 container2 ...}}`

- Remove unused containers, networks, and images:

`docker system prune`

- Fetch and follow the logs of a container:

`docker logs {{[-f|--follow]}} {{container_name}}`
