# docker images

> Gerencia imagens Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Lista todas as imagens Docker:

`docker images`

- Lista todas as imagens Docker incluindo imagens intermedirárias:

`docker images {{[-a|--all]}}`

- Lista no modo silencioso (somente IDs numéricos):

`docker images {{[-q|--quiet]}}`

- Lista todas as imagens Docker não usadas por nenhum container:

`docker images {{[-f|--filter]}} dangling=true`

- Lista imagens que contenham um substring no seu nome:

`docker images "{{*nome*}}"`

- Classifica imagens pelo tamanho:

`docker images --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
