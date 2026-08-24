# apptainer run-help

> Display user-defined help for an Apptainer container image.
> Help text is defined in the `%help` section of the container's definition file.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_run-help.html>.

- Display help for a container:

`apptainer run-help {{path/to/image.sif}}`

- Display help for a specific app within a container:

`apptainer run-help --app {{app_name}} {{path/to/image.sif}}`

- Display help:

`apptainer run-help {{[-h|--help]}}`
