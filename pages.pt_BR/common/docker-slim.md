# docker-slim

> Analisar e otimizar imagens Docker.
> Mais informações: <https://github.com/docker-slim/docker-slim>.

- Iniciar o DockerSlim no modo interativo:

`docker-slim`

- Analisar as camadas do Docker a partir de uma imagem específica:

`docker-slim xray --target {{imagem:tag}}`

- Verificar um Dockerfile:

`docker-slim lint --target {{caminho/para/Dockerfile}}`

- Analisar e gerar uma imagem Docker otimizada:

`docker-slim build {{imagem:tag}}`

- Exibir ajuda para um subcomando:

`docker-slim {{subcomando}} --help`
