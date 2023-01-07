# podman

> Simple management tool for pods, containers and images.
> Podman provides a Docker-CLI comparable command-line. Simply put: `alias docker=podman`.
> More information: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- List all containers (both running and stopped):

`podman ps --all`

- Create a container from an image, with a custom name:

`podman run --name {{container_name}} {{image}}`

- Start or stop an existing container:

`podman {{start|stop}} {{container_name}}`

- Pull an image from a registry (defaults to Docker Hub):

`podman pull {{image}}`

- Display the list of already downloaded images:

`podman images`

- Open a shell inside an already running container:

`podman exec --interactive --tty {{container_name}} {{sh}}`

- Remove a stopped container:

`podman rm {{container_name}}`

- Display the logs of one or more containers and follow log output:

`podman logs --follow {{container_name}} {{container_id}}`
