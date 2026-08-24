# apptainer

> Manage containers for HPC and scientific computing.
> Some subcommands such as `build`, `pull`, and `push` have their own usage documentation.
> More information: <https://apptainer.org/docs/user/main/cli.html>.

- Download a container from Docker Hub:

`apptainer pull {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Download a container from the Container Library:

`apptainer pull {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Build a container from a definition file:

`apptainer build {{path/to/image.sif}} {{path/to/definition.def}}`

- Start an interactive shell inside a container:

`apptainer shell {{path/to/image.sif}}`

- Execute a command inside a container:

`apptainer exec {{path/to/image.sif}} {{command}}`

- Run the default runscript of a container:

`apptainer run {{path/to/image.sif}}`

- Inspect a container's metadata:

`apptainer inspect {{path/to/image.sif}}`

- Display help:

`apptainer {{[-h|--help]}}`
