# docker buildx create

> Create a new builder instance.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/create/>.

- Create a new builder instance using the default Docker context:

`docker buildx create`

- Create a new builder instance with a specific name:

`docker buildx create --name {{builder_name}}`

- Create a new builder instance and immediately set it as the current active builder:

`docker buildx create --name {{builder_name}} --use`

- Create a new builder instance using a specific driver (defaults to `docker`):

`docker buildx create --driver {{docker-container|kubernetes|remote|...}}`

- Create a new builder instance with specific supported platforms:

`docker buildx create --platform {{linux/amd64,linux/arm64,...}}`

- Append a new node to an existing builder:

`docker buildx create --name {{builder_name}} --append {{context|endpoint}}`

- Create a new builder instance with specific BuildKit daemon flags:

`docker buildx create --buildkitd-flags "{{--debug --debugaddr 0.0.0.0:6666}}"`

- Create a new builder instance and boot it immediately:

`docker buildx create --name {{builder_name}} --bootstrap`
