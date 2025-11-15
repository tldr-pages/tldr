# docker exec

> Execute a command on an already running Docker container.
> More information: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Enter an interactive shell session on an already-running container:

`docker exec {{[-it|--interactive --tty]}} {{container_name}} {{/bin/bash}}`

- Run a command in the background (detached) on a running container:

`docker exec {{[-d|--detach]}} {{container_name}} {{command}}`

- Select the working directory for a given command to execute into:

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{path/to/directory}} {{container_name}} {{command}}`

- Run a command in background on existing container but keep `stdin` open:

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- Set an environment variable in a running Bash session:

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Run a command as a specific user:

`docker exec {{[-u|--user]}} {{user}} {{container_name}} {{command}}`
