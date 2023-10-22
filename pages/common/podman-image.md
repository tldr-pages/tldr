# podman image

> Manage Docker images.
> See also `podman build`, `podman import`, and `podman pull`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- List local Docker images:

`podman image ls`

- Delete unused local Docker images:

`podman image prune`

- Delete all unused images (not just those without a tag):

`podman image prune --all`

- Show the history of a local Docker image:

`podman image history {{image}}`
