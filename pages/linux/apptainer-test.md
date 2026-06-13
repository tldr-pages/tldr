# apptainer test

> Run the testscript defined in an Apptainer container image.
> The testscript is defined in the `%test` section of the container's definition file.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_test.html>.

- Run the testscript of a container:

`apptainer test {{path/to/image.sif}}`

- Run the testscript with a bind mount from host to container:

`apptainer test {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- Run the testscript in fully isolated mode (contained filesystem, PID, IPC, and clean environment):

`apptainer test {{[-C|--containall]}} {{path/to/image.sif}}`

- Run the testscript with a writable temporary filesystem overlay:

`apptainer test --writable-tmpfs {{path/to/image.sif}}`

- Run the testscript for a specific app within a container:

`apptainer test --app {{app_name}} {{path/to/image.sif}}`

- Display help:

`apptainer test {{[-h|--help]}}`
