# podman image

> Gerenciar imagens Docker.
> Veja também `podman build`, `podman import` e `podman pull`.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imagens Docker locais:

`podman image ls`

- Exclui imagens Docker locais não utilizadas:

`podman image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`podman image prune --all`

- Mostra o histórico de uma imagem Docker local:

`podman image history {{imagem}}`
