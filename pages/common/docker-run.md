# docker run

> Run a command in a new Docker container.
> More information: <https://docs.docker.com/engine/reference/commandline/run/>.

- Run command in a new container from a tagged image:

`docker run {{image:tag}} {{command}}`

- Run command in a new container in background and display its ID:

`docker run -d {{image}} {{command}}`

- Run command in a one-off container in interactive mode and pseudo-TTY:

`docker run --rm -it {{image}} {{command}}`

- Run command in a new container with passed environment variables:

`docker run -e '{{variable}}={{value}}' -e {{variable}} {{image}} {{command}}`

- Run command in a new container with bind mounted volumes:

`docker run -v {{/path/to/host_path}}:{{/path/to/container_path}} {{image}} {{command}}`

- Run command in a new container with published ports:

`docker run -p {{host_port}}:{{container_port}} {{image}} {{command}}`

- Run command in a new container overwriting the entrypoint of the image:

`docker run --entrypoint {{command}} {{image}}`

- Run command in a new container connecting it to a network:

`docker run --network {{network}} {{image}}`
