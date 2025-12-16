# docker

> Manage Docker containers and images.
> Some subcommands such as `run` have their own usage documentation.
> More information: <https://docs.docker.com/reference/cli/docker/>.

- List all Docker containers (running and stopped):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Start a container from an image, with a custom name:

`docker {{[run|container run]}} --name {{container_name}} {{image}}`

- Start or stop an existing container:

`docker container {{start|stop}} {{container_name}}`

- Pull an image from a Docker registry:

`docker {{[pull|image pull]}} {{image}}`

- Display the list of already downloaded images:

`docker image ls`

- Open an interactive tty with Bourne shell (`sh`) inside a running container:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Remove stopped containers:

`docker {{[rm|container rm]}} {{container1 container2 ...}}`

- Fetch and follow the logs of a container:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_name}}`
