# docker pull

> Baixar imagens do Docker de um registro.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/pull/>.

- Baixar uma imagem específica do Docker:

`docker pull {{imagem}}:{{tag}}`

- Baixar uma imagem específica do Docker no modo silencioso:

`docker pull --quiet {{imagem}}:{{tag}}`

- Baixar todas as tags de uma imagem específica do Docker:

`docker pull --all-tags {{imagem}}`

- Baixar imagens do Docker para uma plataforma específica, por exemplo, linux/amd64:

`docker pull --platform {{linux/amd64}} {{imagem}}:{{tag}}`

- Exibir ajuda:

`docker pull --help`
