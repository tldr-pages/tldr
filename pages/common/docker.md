# docker

> Manage Docker containers and images.

- List currently running docker containers:

`docker ps`

- List all docker containers (running and stopped):

`docker ps -a`

- Start a container from an image, with a custom name:

`docker run --name {{container_name}} {{image}}`

- Start or stop an existing container:

`docker {{start|stop}} {{container_name}}`

- Pull an image from a docker registry:

`docker pull {{image}}`

- Start a container from an image and get a shell inside of it:

`docker run -it {{image}} sh`

- Run a command inside of an already running container:

`docker exec {{container_name}} {{command}}`

- Remove a stopped container:

`docker rm {{container_name}}`

- Fetch and follow the logs of a container:

`docker logs -f {{container_name}}`
