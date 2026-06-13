# apptainer push

> Push container images to remote registries.
> See also: `apptainer-pull`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_push.html>.

- Push a container to the Container Library:

`apptainer push {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Push a container to an OCI registry:

`apptainer push {{path/to/image.sif}} oras://{{registry/namespace/image}}:{{tag}}`

- Push an unsigned container (skip signature verification):

`apptainer push {{[-U|--allow-unsigned]}} {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Push a container with a description (library only):

`apptainer push {{[-D|--description]}} "{{description}}" {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- Display help:

`apptainer push {{[-h|--help]}}`
