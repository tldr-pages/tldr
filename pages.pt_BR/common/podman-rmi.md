# podman rmi

> Remover uma ou mais imagens do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Remover uma ou mais imagens pelo nome delas:

`podman rmi {{imagem:tag}} {{imagem2:tag}} {{...}}`

- Remover uma imagem forçadamente:

`podman rmi --force {{imagem}}`

- Remover uma imagem sem excluir os pais não marcados:

`podman rmi --no-prune {{imagem}}`

- Exibir ajuda:

`podman rmi`
