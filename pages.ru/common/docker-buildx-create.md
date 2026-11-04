# docker buildx create

> Создавать новый экземпляр сборщика.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/create/>.

- Создать новый экземпляр сборщика с использованием контекста Docker по умолчанию:

`docker buildx create`

- Создать новый экземпляр сборщика с определённым именем:

`docker buildx create --name {{имя_сборщика}}`

- Создать новый экземпляр сборщика и сразу установить его как текущий активный:

`docker buildx create --name {{имя_сборщика}} --use`

- Создать новый экземпляр сборщика с использованием определённого драйвера (по умолчанию `docker`):

`docker buildx create --driver {{docker-container|kubernetes|remote|...}}`

- Создать новый экземпляр сборщика с определёнными поддерживаемыми платформами:

`docker buildx create --platform {{linux/amd64,linux/arm64,...}}`

- Добавить новый узел к существующему сборщику:

`docker buildx create --name {{имя_сборщика}} --append {{контекст|точка_подключения}}`

- Создать новый экземпляр сборщика с определёнными флагами демона BuildKit:

`docker buildx create --buildkitd-flags "{{--debug --debugaddr 0.0.0.0:6666}}"`

- Создать новый экземпляр сборщика и сразу запустить его:

`docker buildx create --name {{имя_сборщика}} --bootstrap`
