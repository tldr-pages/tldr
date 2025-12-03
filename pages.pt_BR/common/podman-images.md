# podman images

> Gerenciar imagens do OCI/Docker.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas as imagens do OCI/Docker:

`podman images`

- Lista todas as imagens do OCI/Docker, incluindo intermediárias:

`podman images {{[-a|--all]}}`

- Lista a saída no modo silencioso (apenas IDs numéricos):

`podman images {{[-q|--quiet]}}`

- Lista todas as imagens do OCI/Docker que não são utilizadas por nenhum contêiner:

`podman images {{[-f|--filter]}} dangling=true`

- Lista imagens que contenham uma substring em seus nomes:

`podman images "{{*imagem|imagem*}}"`
