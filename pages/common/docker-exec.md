# docker exec

> Execute a command on an already running Docker container.
> More information: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Enter an interactive shell session on an already-running container:

`docker exec -it {{container-name}} /bin/sh`

- Enter an interactive bash pseudo-TTY on an already-running container:

`docker exec -it {{container-name}} /bin/bash`

- Run a command in the background (detached) on a running container:

`docker exec -d {{container-name}} {{command}}`

- Create a directory in the background on a running container:

`docker exec -d {{container-name}} mkdir {{directory-path}}`

- Select the working directory for a given command to execute into:

`docker exec -it -w {{path/to/directory}} {{container-name}} {{command}}`

- Run a command in background on existing container but keep STDIN open:

`docker exec -i -d {{container-name}} {{command}}`

- Set an environment variable in a running bash session:

`docker exec -it -e {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`
