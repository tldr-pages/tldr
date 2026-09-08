# docker buildx ls

> Lista as instâncias de builder e os nós associados.
> Mais informações: <https://docs.docker.com/reference/cli/docker/buildx/ls/>.

- Lista as instâncias de builder:

`docker buildx ls`

- Formata a saída usando um template Go:

`docker buildx ls --format "{{.NAME}}: {{.DriverEndpoint}}"`
