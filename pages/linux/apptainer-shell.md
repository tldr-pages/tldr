# apptainer shell

> Start an interactive shell within an Apptainer container.
> See also: `apptainer exec`, `apptainer run`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_shell.html>.

- Start an interactive shell inside a container:

`apptainer shell {{path/to/image.sif}}`

- Start a shell with a bind mount from host to container:

`apptainer shell {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- Start a shell with environment variables:

`apptainer shell --env {{variable}}={{value}} {{path/to/image.sif}}`

- Start a shell in fully isolated mode (contained filesystem, PID, IPC, and clean environment):

`apptainer shell {{[-C|--containall]}} {{path/to/image.sif}}`

- Start a shell with a writable temporary filesystem overlay:

`apptainer shell --writable-tmpfs {{path/to/image.sif}}`

- Start a shell with NVIDIA GPU support:

`apptainer shell --nv {{path/to/image.sif}}`

- Start a shell using a specific shell program:

`apptainer shell {{[-s|--shell]}} {{path/to/shell}} {{path/to/image.sif}}`

- Display help:

`apptainer shell {{[-h|--help]}}`
