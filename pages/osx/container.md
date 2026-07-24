# container

> Create and run Linux containers as lightweight virtual machines on macOS.
> More information: <https://github.com/apple/container>.

- Start the container services (required before running containers):

`container system start`

- Run a container from an image interactively and remove it after it exits:

`container run --rm {{[-i|--interactive]}} {{[-t|--tty]}} {{image}} {{sh}}`

- Run a container in the background with a name and a published port:

`container run {{[-d|--detach]}} --name {{container_name}} {{[-p|--publish]}} {{8080:80}} {{image}}`

- Execute a command inside a running container:

`container exec {{[-i|--interactive]}} {{[-t|--tty]}} {{container_name}} {{sh}}`

- List all containers (running and stopped):

`container {{[ls|list]}} {{[-a|--all]}}`

- Follow the logs of a container:

`container logs {{[-f|--follow]}} {{container_name}}`

- Build an image from a Dockerfile in a directory:

`container build {{[-t|--tag]}} {{image_name}} {{path/to/directory}}`

- Stop or delete a container:

`container {{stop|delete}} {{container_name}}`
