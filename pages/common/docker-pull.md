# docker pull

> Download Docker images from a registry.
> More information: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Download a specific Docker image:

`docker pull {{image}}:{{tag}}`

- Download a specific Docker image in quiet mode:

`docker pull {{[-q|--quiet]}} {{image}}:{{tag}}`

- Download all tags of a specific Docker image:

`docker pull {{[-a|--all-tags]}} {{image}}`

- Download a Docker images for a specific platform, e.g. linux/amd64:

`docker pull --platform {{linux/amd64}} {{image}}:{{tag}}`

- Display help:

`docker pull {{[-h|--help]}}`
