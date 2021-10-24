# docker rmi

> Remove uma ou mais imagens Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Exibe a ajuda:

`docker rmi`

- Remove uma ou mais imagens pelo seus nomes:

`docker rmi {{imagem1 imagem2 ...}}`

- Remove forçadamente uma imagem:

`docker rmi --force {{imagem}}`

- Remove uma imagem sem apagar suas imagens pais que não possuem tags:

`docker rmi --no-prune {{imagem}}`
