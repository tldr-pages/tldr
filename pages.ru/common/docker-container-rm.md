# docker container rm

> Удалять контейнеры.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Удалить контейнеры:

`docker {{[rm|container rm]}} {{контейнер1 контейнер2 ...}}`

- Принудительно удалить контейнер:

`docker {{[rm|container rm]}} {{[-f|--force]}} {{контейнер1 контейнер2 ...}}`

- Удалить контейнер и связанные с ним тома:

`docker {{[rm|container rm]}} {{[-v|--volumes]}} {{контейнер}}`

- Показать справку:

`docker {{[rm|container rm]}} {{[-h|--help]}}`
