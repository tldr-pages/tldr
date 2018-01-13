# docker

> Manage Docker containers and images.

- List currently running docker containers:

`docker container ls`

- List all docker containers (running and stopped):

`docker container ls -a`

- Start a container:

`docker container start {{container}}`

- Stop a container:

`docker container stop {{container}}`

- Start a container from an image and get a shell inside of it:

`docker container run -it {{image}} bash`

- Run a command inside of an already running container:

`docker container exec -i {{container}} {{command}}`

- Remove a stopped container:

`docker container rm {{container}}`

- Fetch and follow the logs of a container:

`docker container logs -f {{container}}`

- List all docker images:

`docker images`

- Delete docker image:

`docker rmi {{image}}`

- Pull image from docker-registry:

`docker pull {{image}}`

- Remove unused docker images:

`docker rmi $(docker images | grep none)`

- Show low-level information about container or image:

`docker inspect {{container|image}}`

- Display a live stream of containers' resource usage statistics:

`docker stats $(docker ps -q)`
