# docker image

> Gerencia imagens do Docker.
> Veja também `docker build`, `docker import` e `docker pull`.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/image/>.

- Lista imagens Docker locais:

`docker image ls`

- Exclui imagens Docker locais não utilizadas:

`docker image prune`

- Exclui todas as imagens não utilizadas (não apenas aquelas sem uma etiqueta):

`docker image prune --all`

- Mostra o histórico de uma imagem Docker local:

`docker image history {{imagem}}`
