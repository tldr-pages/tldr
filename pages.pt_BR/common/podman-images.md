# podman images

> Gerenciar imagens de contêineres OCI/Docker.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas as imagens de contêineres:

`podman images`

- Lista todas as imagens de contêiner, incluindo intermediárias:

`podman images {{[-a|--all]}}`

- Lista a saída no modo silencioso (apenas IDs numéricos):

`podman images {{[-q|--quiet]}}`

- Lista todas as imagens de contêiner que não são utilizadas por nenhum contêiner:

`podman images {{[-f|--filter]}} dangling=true`

- Lista imagens que contenham uma substring em seus nomes:

`podman images "{{*imagem|imagem*}}"`
