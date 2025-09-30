# docker start

> Start stopped containers.
> More information: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Display help:

`docker start --help`

- Start a Docker container:

`docker start {{container}}`

- Start a container, attaching `stdout` and `stderr` and forwarding signals:

`docker start {{[-a|--attach]}} {{container}}`

- Start one or more containers:

`docker start {{container1 container2 ...}}`
