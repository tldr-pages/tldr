# docker container stop

> Stop one or more running containers.
> More information: <https://docs.docker.com/reference/cli/docker/container/stop/>.

- Stop a Docker container:

`docker {{[stop|container stop]}} {{container}}`

- Stop a container, sending a specific signal to it:

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{signal}} {{container}}`

- Stop a container, waiting a specific number of seconds before forcibly killing it:

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{seconds}} {{container}}`

- Stop one or more containers:

`docker {{[stop|container stop]}} {{container1 container2 ...}}`

- Display help:

`docker {{[stop|container stop]}} --help`
