# docker context

> Переключаться между контекстами для управления несколькими окружениями Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/context/>.

- Создать контекст с использованием определённой конечной точки Docker:

`docker context create {{имя_контекста}} --docker "host={{tcp://удалённый-хост:2375}}"`

- Создать контекст на основе переменной окружения `$DOCKER_HOST`:

`docker context create {{имя_контекста}}`

- Переключиться на контекст:

`docker context use {{имя_контекста}}`

- Вывести список всех контекстов:

`docker context ls`
