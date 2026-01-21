# apptainer run

> Run the default runscript of an Apptainer container.
> See also: `apptainer exec`, `apptainer shell`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_run.html>.

- Run the default runscript of a container:

`apptainer run {{path/to/image.sif}}`

- Run with arguments passed to the runscript:

`apptainer run {{path/to/image.sif}} {{arg1 arg2 ...}}`

- Run with a bind mount from host to container:

`apptainer run {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- Run with environment variables:

`apptainer run --env {{variable}}={{value}} {{path/to/image.sif}}`

- Run in fully isolated mode (contained filesystem, PID, IPC, and clean environment):

`apptainer run {{[-C|--containall]}} {{path/to/image.sif}}`

- Run with a writable temporary filesystem overlay:

`apptainer run --writable-tmpfs {{path/to/image.sif}}`

- Run with NVIDIA GPU support:

`apptainer run --nv {{path/to/image.sif}}`

- Display help:

`apptainer run {{[-h|--help]}}`
