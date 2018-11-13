# docker

> Manage Docker containers and images.

- List currently running docker containers:

`docker container ls`

- List all docker containers (running and stopped):

`docker container ls -a`

- Start a container from an image, with a custom name:

`docker container run --name={{container_name}} {{image}}`

- Start or stop an existing container:

`docker container {{start|stop}} {{container_name}}`

- Pull an image from a docker registry:

`docker pull {{image}}`

- Start a container from an image and get a shell inside of it:

`docker container run -it {{image}} bash`

- Run a command inside of an already running container:

`docker container exec {{container_name}} {{command}}`

- Remove a stopped container:

`docker container rm {{container_name}}`

- Fetch and follow the logs of a container:

`docker container logs -f {{container_name}}`
