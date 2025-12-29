# docker container run

> Run a command in a new Docker container.
> More information: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Run command in a new container from a tagged image:

`docker {{[run|container run]}} {{image:tag}} {{command}}`

- Run command in a new container in background and display its ID:

`docker {{[run|container run]}} {{[-d|--detach]}} {{image}} {{command}}`

- Run command in a one-off container in interactive mode and pseudo-TTY:

`docker {{[run|container run]}} --rm {{[-it|--interactive --tty]}} {{image}} {{command}}`

- Run command in a new container with passed environment variables:

`docker {{[run|container run]}} {{[-e|--env]}} '{{variable}}={{value}}' {{[-e|--env]}} {{variable}} {{image}} {{command}}`

- Run command in a new container with bind mounted volumes:

`docker {{[run|container run]}} {{[-v|--volume]}} /{{path/to/host_path}}:/{{path/to/container_path}} {{image}} {{command}}`

- Run command in a new container with published ports:

`docker {{[run|container run]}} {{[-p|--publish]}} {{host_port}}:{{container_port}} {{image}} {{command}}`

- Run command in a new container overwriting the entrypoint of the image:

`docker {{[run|container run]}} --entrypoint {{command}} {{image}}`

- Run command in a new container connecting it to a network:

`docker {{[run|container run]}} --network {{network}} {{image}}`
