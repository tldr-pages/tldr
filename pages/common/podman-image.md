# podman image

> Manage OCI/Docker container images.
> See also: `podman build`, `podman import`, `podman pull`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- List local container images:

`podman image {{[ls|list]}}`

- Delete unused local container images:

`podman image prune`

- Delete all unused images (not just those without a tag):

`podman image prune {{[-a|--all]}}`

- Show the history of a local image:

`podman image history {{image}}`
