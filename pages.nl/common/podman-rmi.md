# podman rmi

> Verwijder OCI/Docker-images.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Verwijder een of meer images op basis van hun naam:

`podman rmi {{image1:tag image2:tag ...}}`

- Forceer het verwijderen van een image:

`podman rmi {{[-f|--force]}} {{image}}`

- Verwijder een image zonder ongetagde ouders te verwijderen:

`podman rmi --no-prune {{image}}`

- Toon de help:

`podman rmi {{[-h|--help]}}`
