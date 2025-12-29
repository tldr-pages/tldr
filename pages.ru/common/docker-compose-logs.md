# docker compose logs

> Просмотр вывода контейнеров в Docker Compose приложении.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- Просмотр логов всех сервисов:

`docker compose logs`

- Просмотр логов конкретного сервиса:

`docker compose logs {{имя_сервиса}}`

- Просмотр логов и отслеживание нового вывода (как `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Просмотр логов с временными метками:

`docker compose logs {{[-t|--timestamps]}}`

- Просмотр только последних `n` строк логов для каждого контейнера:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Просмотр логов начиная с определённого времени:

`docker compose logs --since {{временная_метка}}`

- Просмотр логов до определённого времени:

`docker compose logs --until {{временная_метка}}`

- Просмотр логов нескольких конкретных сервисов:

`docker compose logs {{сервис1 сервис2 ...}}`
