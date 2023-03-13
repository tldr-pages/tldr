# podman rmi

> Remove one or more Podman images.
> More information: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remove one or more images given their names:

`podman rmi {{image:tag}} {{image2:tag}} {{...}}`

- Force remove an image:

`podman rmi --force {{image}}`

- Remove an image without deleting untagged parents:

`podman rmi --no-prune {{image}}`

- Display help:

`podman rmi`
