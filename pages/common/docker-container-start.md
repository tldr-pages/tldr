# docker container start

> Start stopped containers.
> More information: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Start a Docker container:

`docker {{[start|container start]}} {{container}}`

- Start a container, attaching `stdout` and `stderr`, and forwarding signals:

`docker {{[start|container start]}} {{[-a|--attach]}} {{container}}`

- Start one or more containers:

`docker {{[start|container start]}} {{container1 container2 ...}}`

- Display help:

`docker {{[start|container start]}} --help`
