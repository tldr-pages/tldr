# docker

> Manage Docker containers and images.

- List currently running docker containers:
`docker ps`

- Start or stop a container:

`docker start|stop {{container}}`

- Start a container from an image and get a shell inside of it:

`docker run -it {{image}} bash`

- Run a command inside an already running container:

`docker exec {{container}} {{command}}`

- Remove a container:

`docker rm {{container}}`

- Remove all containers:

`docker rm $(docker ps -a -q)`

- Remove an image:

`docker rmi {{image}}`

- Remove unused (dangling) images:

`docker rmi $(docker images -q -f dangling=true)`
