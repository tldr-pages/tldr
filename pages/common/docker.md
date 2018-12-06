# docker

> Manage Docker containers and images.

- List currently running docker containers:

`docker ps`

- List all docker containers (running and stopped):

`docker ps -a`

- Start a container from an image, with a custom name:

`docker run -it --name {{container_name}} {{image}}`

- Start or stop an existing container:

`docker {{start|stop}} {{container_name}}`

- Pull an image from a docker registry:

`docker pull {{image}}`

- Run a command inside of an already running container:

`docker exec -it {{container_name}} {{command}}`

- Remove a stopped container:

`docker rm {{container_name}}`

- Fetch and follow the logs of a container:

`docker logs -f {{container_name}}`
