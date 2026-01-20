# docker container logs

> Выводить логи контейнера.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Вывести логи контейнера:

`docker {{[logs|container logs]}} {{имя_контейнера}}`

- Вывести логи и следить за ними (читать в реальном времени):

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{имя_контейнера}}`

- Вывести последние 5 строк:

`docker {{[logs|container logs]}} {{имя_контейнера}} {{[-n|--tail]}} 5`

- Вывести логи, добавляя к ним временные метки:

`docker {{[logs|container logs]}} {{[-t|--timestamps]}} {{имя_контейнера}}`

- Вывести логи до определённого момента времени выполнения контейнера (например, 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{имя_контейнера}} --until {{время}}`
