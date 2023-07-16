# docker image

> Gerenciar imagens do Docker.
> Veja também `docker build`, `docker import` e `docker pull`.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/image/>.

- Listar imagens Docker locais:

`docker image ls`

- Excluir imagens Docker locais não utilizadas:

`docker image prune`

- Excluir todas as imagens não utilizadas (não apenas aquelas sem uma tag):

`docker image prune --all`

- Mostrar o histórico de uma imagem Docker local:

`docker image history {{imagem}}`
