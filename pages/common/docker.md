# docker

> Docker allows you to package an application with all of its
> dependencies into a standardized unit for software development.

- List of running docker containsers

`docker ps`

- List all docker containers (running and stopped)

`docker ps -a`

- List containers by status(created|restarting|running|paused|exited)

`docker ps --filter status={{status}}`

- List only the numeric IDs of containers

`docker ps -q`

- Start a container by id

`docker start {{container_id}}`

- Stop a container

`docker stop {{container_id}}`

- Stop all running containers

`docker stop $(docker ps --filter status=running -q)`

- Remove all containers

`docker rm $(docker ps -a -q)`

- List all docker images (including intermediate images)

`docker images -a`

- Remove all images

`docker rmi $(docker images -q)`