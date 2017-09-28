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

`docker container exec {{container}} {{command}}`

- Remove a stopped container:

`docker container rm {{container}}`
