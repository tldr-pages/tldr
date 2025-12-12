# podman image

> Gerenciar imagens de contêineres OCI/Docker.
> Veja também `podman build`, `podman import` e `podman pull`.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imagens de contêineres locais:

`podman image {{[ls|list]}}`

- Exclui imagens de contêiner locais não utilizadas:

`podman image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`podman image prune {{[-a|--all]}}`

- Exibir o histórico de uma imagem de contêiner local:

`podman image history {{imagem}}`
