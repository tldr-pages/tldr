# docker compose down

> Остановка и удаление контейнеров, сетей, образов и томов, созданных командой `docker compose up`.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/down/>.

- Остановить и удалить все контейнеры и сети:

`docker compose down`

- Остановить и удалить контейнеры, сети и все образы, используемые сервисами:

`docker compose down --rmi all`

- Остановить и удалить контейнеры, сети и только образы без пользовательского тега:

`docker compose down --rmi local`

- Остановить и удалить контейнеры, сети и все тома:

`docker compose down {{[-v|--volumes]}}`

- Остановить и удалить всё, включая осиротевшие контейнеры:

`docker compose down --remove-orphans`

- Остановить и удалить контейнеры с использованием альтернативного Compose-файла:

`docker compose {{[-f|--file]}} {{путь/к/файлу}} down`

- Остановить и удалить контейнеры с указанием таймаута в секундах:

`docker compose down {{[-t|--timeout]}} {{таймаут}}`

- Удалить контейнеры для сервисов, не определённых в Compose-файле:

`docker compose down --remove-orphans {{[-v|--volumes]}}`
