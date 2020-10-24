# docker exec

> Execute a command on an already running Docker container.
> More information: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Enter an interactive shell session on an already-running container:

`docker exec -it {{container_name}} {{/bin/bash}}`

- Run a command in the background (detached) on a running container:

`docker exec -d {{container_name}} {{command}}`

- Select the working directory for a given command to execute into:

`docker exec -it -w {{path/to/directory}} {{container_name}} {{command}}`

- Run a command in background on existing container but keep `stdin` open:

`docker exec -i -d {{container_name}} {{command}}`

- Set an environment variable in a running bash session:

`docker exec -it -e {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`
