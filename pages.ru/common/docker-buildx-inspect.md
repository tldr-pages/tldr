# docker buildx inspect

> Показывать информацию о текущем или указанном экземпляре сборщика.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/inspect>.

- Показать информацию о текущем экземпляре сборщика:

`docker buildx inspect`

- Показать информацию об указанном экземпляре сборщика по имени:

`docker buildx inspect {{имя_сборщика}}`

- Убедиться, что сборщик запущен перед проверкой:

`docker buildx inspect --bootstrap`

- Переопределить таймаут загрузки статуса сборщика (по умолчанию 20 секунд):

`docker buildx inspect --timeout {{секунды}}`
