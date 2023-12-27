# docker start

> Start one or more stopped containers.
> More information: <https://docs.docker.com/engine/reference/commandline/start/>.

- Display help:

`docker start`

- Start a docker container:

`docker start {{container}}`

- Start a container, attaching `stdout` and `stderr` and forwarding signals:

`docker start --attach {{container}}`

- Start one or more space-separated containers:

`docker start {{container1 container2 ...}}`
