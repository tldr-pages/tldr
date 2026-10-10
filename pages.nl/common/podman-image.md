# podman image

> Beheer OCI/Docker container-images.
> Zie ook: `podman build`, `podman import`, `podman pull`.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Toon lokale container-images:

`podman image {{[ls|list]}}`

- Verwijder ongebruikte lokale container-images:

`podman image prune`

- Verwijder alle ongebruikte images (niet alleen die zonder tag):

`podman image prune {{[-a|--all]}}`

- Toon de geschiedenis van een lokale container-image:

`podman image history {{image}}`
