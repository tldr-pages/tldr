# docker compose start

> Запускать существующие контейнеры для сервисов.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/start/>.

- Запустить существующие контейнеры для всех сервисов:

`docker compose start`

- Запустить существующие контейнеры для одного или нескольких сервисов:

`docker compose start {{сервис1 сервис2 ...}}`

- Симулировать запуск существующих контейнеров:

`docker compose start --dry-run`

- Запустить существующие контейнеры и ждать, пока сервисы будут запущены или здоровы:

`docker compose start --wait`

- Запустить существующие контейнеры и ждать указанное количество секунд:

`docker compose start --wait --wait-timeout {{секунды}}`
