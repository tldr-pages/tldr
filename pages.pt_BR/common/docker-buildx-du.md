# docker buildx du

> Exibe o uso de disco de um builder.
> Mais informações: <https://docs.docker.com/reference/cli/docker/buildx/du/>.

- Exibe o uso de disco:

`docker buildx du`

- Filtra a saída com base em uma condição específica:

`docker buildx du --filter "{{description~=golang}}"`

- Exibe uma saída detalhada:

`docker buildx du --verbose`

- Formata a saída usando um template Go:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- Exibe a saída formatada como JSON com o comando `jq`:

`docker buildx du --format json | jq .`

- Exibe o uso de disco de um builder específico:

`docker buildx du --builder {{nome_do_builder}}`
