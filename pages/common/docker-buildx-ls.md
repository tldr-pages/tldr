# docker buildx ls

> List builder instances and associated nodes.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/ls/>.

- List builder instances:

`docker buildx ls`

- Format the output using a Go template:

`docker buildx ls --format "{{.NAME}}: {{.DriverEndpoint}}"`
