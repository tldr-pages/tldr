# docker image

> Управлять образами Docker.
> Смотрите также: `docker build`, `docker image pull`, `docker image rm`.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/>.

- Вывести список локальных образов Docker:

`docker {{[images|image ls]}}`

- Удалить неиспользуемые локальные образы Docker:

`docker image prune`

- Удалить все неиспользуемые образы (не только без тегов):

`docker image prune {{[-a|--all]}}`

- Показать историю локального образа Docker:

`docker {{[history|image history]}} {{образ}}`
