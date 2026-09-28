# docker buildx rm

> Remove uma ou mais instâncias de builder.
> Mais informações: <https://docs.docker.com/reference/cli/docker/buildx/rm/>.

- Remove uma instância de builder:

`docker buildx rm {{nome_do_builder}}`

- Remove todos os builders inativos:

`docker buildx rm --all-inactive`

- Remove todos os builders inativos sem pedir confirmação:

`docker buildx rm --all-inactive {{[-f|--force]}}`
