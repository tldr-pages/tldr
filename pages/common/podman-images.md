# podman images

> Manage OCI/Docker container images.
> More information: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- List all container images:

`podman images`

- List all container images including intermediates:

`podman images {{[-a|--all]}}`

- List the output in quiet mode (only numeric IDs):

`podman images {{[-q|--quiet]}}`

- List all images not used by any container:

`podman images {{[-f|--filter]}} dangling=true`

- List images that contain a substring in their name:

`podman images "{{*image|image*}}"`
