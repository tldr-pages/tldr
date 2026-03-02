# docker buildx ls

> List builder instances and associated nodes.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/ls/>.

- List builder instances:

`docker buildx ls`

- Format output:

`docker buildx ls --format "{{.NAME}}: {{.DriverEndpoint}}"`
