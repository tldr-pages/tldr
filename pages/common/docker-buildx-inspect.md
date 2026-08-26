# docker buildx inspect

> Inspect the current or a specified builder instance.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/inspect/>.

- Show information about the current builder instance:

`docker buildx inspect`

- Inspect a specific builder instance by name:

`docker buildx inspect {{builder_name}}`

- Ensure the builder is running before inspecting:

`docker buildx inspect --bootstrap`

- Override the default timeout for loading builder status (default: 20 seconds):

`docker buildx inspect --timeout {{seconds}}`
