# podman export

> Export the filesystem of a container and save it as a tarball on the local machine.
> See also: `podman import`, `podman save`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-export.1.html>.

- Export a container's filesystem to a tar file:

`podman export {{[-o|--output]}} {{path/to/file.tar}} {{container_name_or_id}}`

- Export a container's filesystem to stdout:

`podman export {{container_name_or_id}} > {{path/to/file.tar}}`
