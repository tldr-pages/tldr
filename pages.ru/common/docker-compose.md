# docker compose

> Запуск и управление многоконтейнерными Docker-приложениями.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/>.

- Список всех запущенных контейнеров:

`docker compose ps`

- Создать и запустить все контейнеры в фоновом режиме, используя файл `docker-compose.yml` из текущей директории:

`docker compose up {{[-d|--detach]}}`

- Запустить все контейнеры, пересобрать при необходимости:

`docker compose up --build`

- Запустить все контейнеры, указав имя проекта и альтернативный Compose-файл:

`docker compose {{[-p|--project-name]}} {{имя_проекта}} {{[-f|--file]}} {{путь/к/файлу}} up`

- Остановить все запущенные контейнеры:

`docker compose stop`

- Остановить и удалить все контейнеры, сети, образы и тома:

`docker compose down --rmi all {{[-v|--volumes]}}`

- Следить за логами всех контейнеров:

`docker compose logs {{[-f|--follow]}}`

- Следить за логами конкретного контейнера:

`docker compose logs {{[-f|--follow]}} {{имя_контейнера}}`
