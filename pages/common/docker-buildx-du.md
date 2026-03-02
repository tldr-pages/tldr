# docker buildx du

> See disk usage for a builder.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/du/>.

- Show disk usage:

`docker buildx du`

- Filter output using `<key><operator><value>` format:

`docker buildx du --filter "description~=golang"`

- Pretty print output:

`docker buildx du --verbose`

- Format output using placeholder values:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- Pretty print output as JSON with `jq` command:

`docker buildx du --format=json | jq .`

- Inspect the disk usage of a specific builder:

`docker buildx due --builder mybuilder`
