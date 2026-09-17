# apptainer exec

> Execute a command within an Apptainer container.
> See also: `apptainer run`, `apptainer shell`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_exec.html>.

- Execute a command inside a container:

`apptainer exec {{path/to/image.sif}} {{command}}`

- Execute a command with arguments:

`apptainer exec {{path/to/image.sif}} {{command}} {{arg1 arg2 ...}}`

- Execute a command with a bind mount from host to container:

`apptainer exec {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}} {{command}}`

- Execute a command with environment variables:

`apptainer exec --env {{variable}}={{value}} {{path/to/image.sif}} {{command}}`

- Execute a command in fully isolated mode (contained filesystem, PID, IPC, and clean environment):

`apptainer exec {{[-C|--containall]}} {{path/to/image.sif}} {{command}}`

- Execute a command with a writable temporary filesystem overlay:

`apptainer exec --writable-tmpfs {{path/to/image.sif}} {{command}}`

- Execute a command with NVIDIA GPU support:

`apptainer exec --nv {{path/to/image.sif}} {{command}}`

- Display help:

`apptainer exec {{[-h|--help]}}`
