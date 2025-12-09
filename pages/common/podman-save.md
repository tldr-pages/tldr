# podman save

> Save an image to a local file or directory.
> See also: `podman load`, `podman export`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-save.1.html>.

- Save an image to a tar file:

`podman save {{[-o|--output]}} {{path/to/file.tar}} {{image:tag}}`

- Save an image to `stdout`:

`podman save {{image:tag}} > {{path/to/file.tar}}`
