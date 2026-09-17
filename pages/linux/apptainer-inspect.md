# apptainer inspect

> Display metadata of Apptainer container images.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_inspect.html>.

- Show the labels of an image (default):

`apptainer inspect {{path/to/image.sif}}`

- Show the definition file used to build the image:

`apptainer inspect {{[-d|--deffile]}} {{path/to/image.sif}}`

- Show the runscript for the image:

`apptainer inspect {{[-r|--runscript]}} {{path/to/image.sif}}`

- Show the environment variables of the image:

`apptainer inspect {{[-e|--environment]}} {{path/to/image.sif}}`

- List all apps in the container:

`apptainer inspect --list-apps {{path/to/image.sif}}`

- Show all available data in JSON format:

`apptainer inspect --all {{path/to/image.sif}}`

- Display help:

`apptainer inspect {{[-h|--help]}}`
