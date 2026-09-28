# docker volume

> Управлять томами Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/volume/>.

- Создать том:

`docker volume create {{имя_тома}}`

- Создать том с определённой меткой:

`docker volume create --label {{метка}} {{имя_тома}}`

- Создать том `tmpfs` размером 100 МиБ и uid 1000:

`docker volume create {{[-o|--opt]}} {{type}}={{tmpfs}} {{[-o|--opt]}} {{device}}={{tmpfs}} {{[-o|--opt]}} {{o}}={{size=100m,uid=1000}} {{имя_тома}}`

- Вывести список всех томов:

`docker volume ls`

- Удалить том:

`docker volume rm {{имя_тома}}`

- Показать информацию о томе:

`docker volume inspect {{имя_тома}}`

- Удалить все неиспользуемые локальные тома:

`docker volume prune`

- Показать справку по подкоманде:

`docker volume {{подкоманда}} --help`
