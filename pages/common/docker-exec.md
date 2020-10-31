# docker exec

> Execute a command on an already running Docker container.
> More information: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Enter an interactive shell session on an already-running container:

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- Run a command in the background (detached) on a running container:

`docker exec --detach {{container_name}} {{command}}`

- Select the working directory for a given command to execute into:

`docker exec --interactive -tty --workdir {{path/to/directory}} {{container_name}} {{command}}`

- Run a command in background on existing container but keep `stdin` open:

`docker exec --interactive --detach {{container_name}} {{command}}`

- Set an environment variable in a running bash session:

`docker exec --interactive --tty --env {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Run a command as a specific user:

`docker exec --user {{user}} {{container_name}} {{command}}`
