# podman build

> Daemonless tool for building container images.
> More information: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Create an image using a `Dockerfile` or `Containerfile` in the specified directory:

`podman build {{path/to/directory}}`

- Create an image with a specified tag:

`podman build {{[-t|--tag]}} {{image_name:version}} {{path/to/directory}}`

- Create an image from a non-standard file:

`podman build {{[-f|--file]}} {{Containerfile.different}} .`

- Create an image without using any previously cached images:

`podman build --no-cache {{path/to/directory}}`

- Create an image suppressing all output:

`podman build {{[-q|--quiet]}} {{path/to/directory}}`
