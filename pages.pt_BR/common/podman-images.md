# podman images

> Gerenciar imagens do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas as imagens do Podman:

`podman images`

- Lista todas as imagens do Podman, incluindo intermediárias:

`podman images --all`

- Lista a saída no modo silencioso (apenas IDs numéricos):

`podman images --quiet`

- Lista todas as imagens do Podman que não são utilizadas por nenhum contêiner:

`podman images --filter dangling=true`

- Lista imagens que contenham uma substring em seus nomes:

`podman images "{{*imagem|imagem*}}"`
