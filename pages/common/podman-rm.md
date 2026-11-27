# podman rm

> Remove one or more containers.
> More information: <https://docs.podman.io/en/latest/markdown/podman-rm.1.html>.

- Remove one or more stopped containers:

`podman rm {{container_name1 container_name2 ...}}`

- Force remove a running or paused container:

`podman rm {{[-f|--force]}} {{container_name}}`

- Remove a container and its anonymous volumes:

`podman rm {{[-v|--volumes]}} {{container_name}}`

- Remove a container and all containers that depend on it:

`podman rm --depend {{container_name}}`

- Remove all stopped containers:

`podman rm --filter status=exited`

- Force remove all containers, regardless of their state:

`podman rm {{[-f|--force]}} {{[-a|--all]}}`

- Remove containers without failing if they do not exist:

`podman rm {{[-i|--ignore]}} {{container_name1 container_name2 ...}}`
