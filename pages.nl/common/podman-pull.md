# podman pull

> Haal images op uit een containerregister.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-pull.1.html>.

- Haal een specifieke container image op:

`podman pull {{image}}:{{tag}}`

- Haal een container image in stille modus op:

`podman pull {{[-q|--quiet]}} {{image}}:{{tag}}`

- Haal alle tags van een container image op:

`podman pull {{[-a|--all-tags]}} {{image}}`

- Haal een container image op voor een specifiek platform:

`podman pull --platform {{linux/arm64}} {{image}}:{{tag}}`

- Haal een container image op zonder TLS-verificatie:

`podman pull --tls-verify=false {{image}}:{{tag}}`

- Toon de help:

`podman pull {{[-h|--help]}}`
