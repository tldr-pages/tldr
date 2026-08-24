# docker buildx du

> See disk usage for a builder.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/du/>.

- Show disk usage:

`docker buildx du`

- Filter output based on a specific condition:

`docker buildx du --filter "{{description~=golang}}"`

- Show verbose output:

`docker buildx du --verbose`

- Format the output using a Go template:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- Pretty print output as JSON with `jq` command:

`docker buildx du --format json | jq .`

- Inspect the disk usage of a specific builder:

`docker buildx du --builder {{builder_name}}`
