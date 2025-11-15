# docker rmi

> Remove uma ou mais imagens Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Exibe a ajuda:

`docker rmi`

- Remove uma ou mais imagens pelo seus nomes:

`docker rmi {{imagem1 imagem2 ...}}`

- Remove forçadamente uma imagem:

`docker rmi {{[-f|--force]}} {{imagem}}`

- Remove uma imagem sem apagar suas imagens pais que não possuem tags:

`docker rmi --no-prune {{imagem}}`
