# podman build

> Daemonless tool for building container images.
> Podman provides a Docker-CLI comparable command-line. Simply put: `alias docker=podman`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Create an image using a `Dockerfile` or `Containerfile` in the specified directory:

`podman build {{path/to/directory}}`

- Create an image with a specified tag:

`podman build --tag {{image_name:version}} {{path/to/directory}}`

- Create an image from a non-standard file:

`podman build --file {{Containerfile.different}} .`

- Create an image without using any previously cached images:

`podman build --no-cache {{path/to/directory}}`

- Create an image suppressing all output:

`podman build --quiet {{path/to/directory}}`
