# docker container ls

> Выводить список контейнеров Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Вывести список запущенных контейнеров Docker:

`docker {{[ps|container ls]}}`

- Вывести список всех контейнеров Docker (запущенных и остановленных):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Показать последний созданный контейнер (включая все состояния):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Отфильтровать контейнеры, содержащие подстроку в имени:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{имя}}"`

- Отфильтровать контейнеры, использующие указанный образ в качестве предка (ancestor):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{образ}}:{{тег}}"`

- Отфильтровать контейнеры по коду завершения:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{код}}"`

- Отфильтровать контейнеры по статусу (created, running, removing, paused, exited и dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{статус}}"`

- Отфильтровать контейнеры, которые монтируют определённый том или имеют том, смонтированный по определённому пути:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{путь/к/директории}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
