# docker-slim

> Analisar e otimizar imagens Docker.
> Mais informações: <https://github.com/docker-slim/docker-slim>.

- Inicia o DockerSlim no modo interativo:

`docker-slim`

- Analisa as camadas do Docker a partir de uma imagem específica:

`docker-slim xray --target {{imagem:tag}}`

- Verifica um Dockerfile:

`docker-slim lint --target {{caminho/para/Dockerfile}}`

- Analisa e gera uma imagem Docker otimizada:

`docker-slim build {{imagem:tag}}`

- Exibe ajuda para um subcomando:

`docker-slim {{subcomando}} --help`
