# podman exec

> Execute a command in a running container.
> More information: <https://docs.podman.io/en/latest/markdown/podman-exec.1.html>.

- Open an interactive shell inside a running container:

`podman exec {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Run a command in the background (detached) inside a running container:

`podman exec {{[-d|--detach]}} {{container_name}} {{command}}`

- Run a command in a specific working directory:

`podman exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{path/to/directory}} {{container_name}} {{command}}`

- Run a command as a specific user:

`podman exec {{[-u|--user]}} {{user}} {{container_name}} {{command}}`

- Run a command with an environment variable set:

`podman exec {{[-e|--env]}} {{variable_name}}={{value}} {{container_name}} {{command}}`

- Run a command in the latest created container:

`podman exec {{[-l|--latest]}} {{command}}`
