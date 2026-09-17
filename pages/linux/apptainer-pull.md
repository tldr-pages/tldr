# apptainer pull

> Pull container images from remote sources.
> See also: `apptainer-push`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_pull.html>.

- Pull a container from Docker Hub:

`apptainer pull {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Pull a container from the Container Library:

`apptainer pull {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Pull a container from an OCI registry:

`apptainer pull {{path/to/image.sif}} oras://{{registry/namespace/image}}:{{tag}}`

- Pull a container for a specific architecture:

`apptainer pull --arch {{amd64|arm64|ppc64le}} {{path/to/image.sif}} library://{{image}}:{{tag}}`

- Force overwrite an existing image file:

`apptainer pull {{[-F|--force]}} {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Pull a container as a writable sandbox directory:

`apptainer pull --sandbox {{path/to/directory}} docker://{{image}}:{{tag}}`

- Pull a container without using the cache:

`apptainer pull --disable-cache {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- Display help:

`apptainer pull {{[-h|--help]}}`
