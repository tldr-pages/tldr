# docker buildx rm

> Удалять один или несколько экземпляров сборщиков.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/rm/>.

- Удалить экземпляр сборщика:

`docker buildx rm {{имя_сборщика}}`

- Удалить все неактивные экземпляры сборщиков:

`docker buildx rm --all-inactive`

- Удалить все неактивные экземпляры сборщиков без подтверждения:

`docker buildx rm --all-inactive {{[-f|--force]}}`
