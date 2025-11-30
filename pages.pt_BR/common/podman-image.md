# podman image

> Gerenciar imagens Podman.
> Veja também `podman build`, `podman import` e `podman pull`.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imagens Podman locais:

`podman image {{[ls|list]}}`

- Exclui imagens Podman locais não utilizadas:

`podman image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`podman image prune {{[-a|--all]}}`

- Mostra o histórico de uma imagem Podman local:

`podman image history {{imagem}}`
