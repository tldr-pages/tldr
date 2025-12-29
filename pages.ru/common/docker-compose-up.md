# docker compose up

> Запускать Docker-сервисы, определённые в Compose-файле.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/up/>.

- Запустить все сервисы, определённые в Compose-файле:

`docker compose up`

- Запустить сервисы в фоновом режиме (detached mode):

`docker compose up {{[-d|--detach]}}`

- Запустить сервисы и пересобрать образы перед запуском:

`docker compose up --build`

- Запустить только указанные сервисы:

`docker compose up {{сервис1 сервис2 ...}}`

- Запустить сервисы с указанием альтернативного Compose-файла:

`docker compose {{[-f|--file]}} {{путь/к/файлу}} up`

- Запустить сервисы и удалить осиротевшие контейнеры:

`docker compose up --remove-orphans`

- Запустить сервисы с масштабированием экземпляров:

`docker compose up --scale {{сервис}}={{количество}}`

- Запустить сервисы и показать логи с временными метками:

`docker compose up --timestamps`
