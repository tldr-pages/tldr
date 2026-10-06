# docker image ls

> Выводить список образов Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Вывести список всех образов Docker:

`docker {{[images|image ls]}}`

- Вывести список всех образов Docker, включая промежуточные:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Вывести список в тихом режиме (только числовые идентификаторы):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Вывести список всех образов Docker, не используемых ни одним контейнером:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Вывести список образов, содержащих подстроку в имени:

`docker {{[images|image ls]}} "{{*имя*}}"`

- Отсортировать образы по размеру:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
