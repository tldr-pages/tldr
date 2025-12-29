# docker image pull

> Download Docker-images van een register.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Download een specifiek Docker-image:

`docker {{[pull|image pull]}} {{image}}:{{tag}}`

- Download een specifiek Docker-image in stille modus:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{image}}:{{tag}}`

- Download alle tags van een specifiek Docker image:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{image}}`

- Download een Docker-image voor een specifiek platform, bijv. linux/amd64:

`docker {{[pull|image pull]}} --platform linux/amd64 {{image}}:{{tag}}`

- Toon de help:

`docker {{[pull|image pull]}} {{[-h|--help]}}`
