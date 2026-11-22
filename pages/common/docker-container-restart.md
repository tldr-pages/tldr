# docker container restart

> Restart one or more containers.
> See also: `docker container stop`, `docker container start`.
> More information: <https://docs.docker.com/reference/cli/docker/container/restart/>.

- Restart a container:

`docker {{[restart|container restart]}} {{container}}`

- Restart multiple containers:

`docker {{[restart|container restart]}} {{container1 container2 ...}}`

- Restart a container, waiting a specific number of seconds before forcibly killing it:

`docker {{[restart|container restart]}} {{[-t|--timeout]}} {{seconds}} {{container}}`

- Restart a container, sending a specific signal to stop it:

`docker {{[restart|container restart]}} {{[-s|--signal]}} {{signal}} {{container}}`

- Display help:

`docker {{[restart|container restart]}} --help`
