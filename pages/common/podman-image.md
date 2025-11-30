# podman image

> Manage Podman images.
> See also: `podman build`, `podman import`, `podman pull`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- List local Podman images:

`podman image {{[ls|list]}}`

- Delete unused local Podman images:

`podman image prune`

- Delete all unused images (not just those without a tag):

`podman image prune {{[-a|--all]}}`

- Show the history of a local Podman image:

`podman image history {{image}}`
