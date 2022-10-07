# docker

> Manage Docker containers and images.
> Some subcommands such as `docker run` have their own usage documentation.
> More information: <https://docs.docker.com/engine/reference/commandline/cli/>.

- List all docker containers (running and stopped):

`docker ps --all`

- Start a container from an image, with a custom name:

`docker run --name {{container_name}} {{image}}:{{latest}}`

- Start or stop an existing container:

`docker {{start|stop}} {{container_name}}`

- Pull an image from a docker registry:

`docker pull {{image}}:{{image_tag}}`

- Display the list of already downloaded images:

`docker images`

- Open a shell inside a running container:

`docker exec -it {{container_name}} {{sh}}`

- Remove a stopped container:

`docker rm {{container_name}}`

- Remove an image that does not have a present container:

`docker rmi {{image_name}}:{{image_tag}}`

- Fetch and follow the logs of a container:

`docker logs -f {{container_name}}`
