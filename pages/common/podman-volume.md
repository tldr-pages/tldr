# podman volume

> Manage Podman volumes.
> More information: <https://docs.podman.io/en/latest/markdown/podman-volume.1.html>.

- List local volumes:

`podman volume ls`

- Create a named volume:

`podman volume create {{volume_name}}`

- Export volume content to a `.tar` file:

`podman volume export {{[-o|--output]}} {{path/to/file.tar}} {{volume_name}}`

- Import tarball contents into an existing podman volume:

`podman volume import {{volume_name}} {{path/to/file.tar}}`

- Remove all unused volumes:

`podman volume prune {{[-a|--all]}}`
