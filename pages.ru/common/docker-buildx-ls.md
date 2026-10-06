# docker buildx ls

> Выводить список экземпляров сборщиков и связанных узлов.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/ls/>.

- Вывести список экземпляров сборщиков:

`docker buildx ls`

- Отформатировать вывод с использованием Go-шаблона:

`docker buildx ls --format "{{.NAME}}: {{.DriverEndpoint}}"`
