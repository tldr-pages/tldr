# podman image

> Gerenciar imagens OCI/Docker.
> Veja também `podman build`, `podman import` e `podman pull`.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imagens OCI/Docker locais:

`podman image {{[ls|list]}}`

- Exclui imagens OCI/Docker locais não utilizadas:

`podman image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`podman image prune {{[-a|--all]}}`

- Mostra o histórico de uma imagem OCI/Docker local:

`podman image history {{imagem}}`
