# podman load

> Load an image from an oci-archive or a docker-archive created using podman save.
> See also: `podman image load`, `podman save`, `podman import`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-load.1.html>.

- Create an image from a compressed tar file:

`podman load {{[-i|--input]}} {{path/to/archive}}`

- Suppress the progress output:

`podman load -q -i {{path/to/archive}}`
