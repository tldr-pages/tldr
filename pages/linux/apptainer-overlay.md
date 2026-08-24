# apptainer overlay

> Manage EXT3 writable overlay images for Apptainer containers.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_overlay.html>.

- Add a writable overlay to an existing SIF image:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/to/image.sif}}`

- Create a standalone EXT3 writable overlay image:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/to/overlay.img}}`

- Create a sparse overlay image:

`apptainer overlay create {{[-s|--size]}} {{size}} {{[-S|--sparse]}} {{path/to/overlay.img}}`

- Create an overlay for use with fakeroot:

`apptainer overlay create {{[-f|--fakeroot]}} {{[-s|--size]}} {{size}} {{path/to/overlay.img}}`

- Create an overlay with a specific directory in the layout:

`apptainer overlay create --create-dir {{path/to/directory}} {{path/to/overlay.img}}`

- Display help:

`apptainer overlay {{[-h|--help]}}`
