# apptainer build

> Build Apptainer container images.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- Build a container from a definition file:

`apptainer build {{path/to/image.sif}} {{path/to/definition.def}}`

- Build a container from Docker Hub:

`apptainer build {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Build a container from the Container Library:

`apptainer build {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Build a writable sandbox directory instead of an image file:

`apptainer build {{[-s|--sandbox]}} {{path/to/directory}} docker://{{image}}:{{tag}}`

- Build a container without using the cache:

`apptainer build --disable-cache {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Force overwrite an existing image file:

`apptainer build {{[-F|--force]}} {{path/to/image.sif}} {{path/to/definition.def}}`

- Build using fakeroot for unprivileged builds:

`apptainer build {{[-f|--fakeroot]}} {{path/to/image.sif}} {{path/to/definition.def}}`

- Display help:

`apptainer build {{[-h|--help]}}`
