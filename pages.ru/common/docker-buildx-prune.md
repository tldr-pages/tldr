# docker buildx prune

> Удалять кэш сборки.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/prune/>.

- Удалить кэш сборки для текущего активного сборщика:

`docker buildx prune`

- Удалить записи кэша на основе определённого фильтра:

`docker buildx prune --filter "{{type=source.local}}"`

- Удалить наименее используемые записи кэша до достижения определённого размера кэша:

`docker buildx prune --max-used-space {{128mb}}`

- Удалить наименее используемые записи кэша до достижения определённого объёма свободного места на диске:

`docker buildx prune --reserved-space {{2gb}}`
