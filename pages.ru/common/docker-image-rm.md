# docker image rm

> Удалять образы Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Удалить один или несколько образов по имени:

`docker {{[rmi|image rm]}} {{образ1 образ2 ...}}`

- Принудительно удалить образ:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{образ}}`

- Удалить образ без удаления родительских образов без тегов:

`docker {{[rmi|image rm]}} --no-prune {{образ}}`

- Показать справку:

`docker {{[rmi|image rm]}} --help`
