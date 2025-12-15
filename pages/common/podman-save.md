# podman save

> Save an image to a local file or directory.
> See also: `podman load`, `podman export`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-save.1.html>.

- Save an image to a tar file:

`podman save {{[-o|--output]}} {{path/to/file.tar}} {{image:tag}}`

- Save an image to `stdout`:

`podman save {{image:tag}} > {{path/to/file.tar}}`

- Save an image with compression:

`podman save {{image:tag}} | {{[gzip|bzip2|xz|zstd|zstdchunked]}} > {{path/to/file.tar[.gz|.bz2|.xz|.zst|.zst]}}`

- Save an image, compress it, and transfer to a remote server with progress bar:

`podman save {{image:tag}} | zstd -TO --ultra | pv | ssh {{username}}@{{remote_host}} podman load`
