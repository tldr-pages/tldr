# docker

> Docker allows you to package an application with all of its.
> Dependencies into a standardized unit for software development.

- List of running docker containers:

`docker ps`

- List all docker containers (running and stopped):

`docker ps -a`

- Start a container:

`docker start {{container}}`

- Stop a container:

`docker stop {{container}}`

- Start a container from an image and get a shell inside of it:

`docker run -it {{image}} bash`

- Run a command inside of an already running container:

`docker exec {{container}} {{command}}`
