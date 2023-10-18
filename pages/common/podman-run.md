# podman run

> Run a command in a new Podman container.
> More information: <https://docs.podman.io/en/latest/markdown/podman-run.1.html>.

- Run command in a new container from a tagged image:

`podman run {{image:tag}} {{command}}`

- Run command in a new container in background and display its ID:

`podman run --detach {{image:tag}} {{command}}`

- Run command in a one-off container in interactive mode and pseudo-TTY:

`podman run --rm --interactive --tty {{image:tag}} {{command}}`

- Run command in a new container with passed environment variables:

`podman run --env '{{variable}}={{value}}' --env {{variable}} {{image:tag}} {{command}}`

- Run command in a new container with bind mounted volumes:

`podman run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image:tag}} {{command}}`

- Run command in a new container with published ports:

`podman run --publish {{host_port}}:{{container_port}} {{image:tag}} {{command}}`

- Run command in a new container overwriting the entrypoint of the image:

`podman run --entrypoint {{command}} {{image:tag}}`

- Run command in a new container connecting it to a network:

`podman run --network {{network}} {{image:tag}}`
