# podman load

> Load an image from an oci-archive or a docker-archive created using podman save.
> See also: `podman save`, `podman import`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-load.1.html>.

- Load an image from a tar file:

`podman load {{[-i|--input]}} {{path/to/file.tar}}`

- Load an image and display quiet output (only show the image ID):

`podman load {{[-q|--quiet]}} {{[-i|--input]}} {{path/to/file.tar}}`

- Load an image from `stdin`:

`podman load < {{path/to/file.tar}}`
