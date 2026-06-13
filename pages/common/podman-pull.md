# podman pull

> Pull images from a container registry.
> More information: <https://docs.podman.io/en/latest/markdown/podman-pull.1.html>.

- Pull a specific container image:

`podman pull {{image}}:{{tag}}`

- Pull a container image in quiet mode:

`podman pull {{[-q|--quiet]}} {{image}}:{{tag}}`

- Pull all tags of a container image:

`podman pull {{[-a|--all-tags]}} {{image}}`

- Pull a container image for a specific platform:

`podman pull --platform {{linux/arm64}} {{image}}:{{tag}}`

- Pull a container image without TLS verification:

`podman pull --tls-verify=false {{image}}:{{tag}}`

- Display help:

`podman pull {{[-h|--help]}}`
