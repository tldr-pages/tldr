# docker image pull

> Baixar imagens do Docker de um registro.
> Mais informações: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Baixa uma imagem específica do Docker:

`docker {{[pull|image pull]}} {{imagem}}:{{tag}}`

- Baixa uma imagem específica do Docker no modo silencioso:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{imagem}}:{{tag}}`

- Baixa todas as tags de uma imagem específica do Docker:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{imagem}}`

- Baixa imagens do Docker para uma plataforma específica, por exemplo, linux/amd64:

`docker {{[pull|image pull]}} --platform linux/amd64 {{imagem}}:{{tag}}`

- Exibe ajuda:

`docker {{[pull|image pull]}} {{[-h|--help]}}`
