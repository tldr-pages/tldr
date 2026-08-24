# docker compose logs

> Просматривать вывод контейнеров в Docker Compose приложении.
> Больше информации: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- Просмотреть логи всех сервисов:

`docker compose logs`

- Просмотреть логи конкретного сервиса:

`docker compose logs {{имя_сервиса}}`

- Просмотреть логи и отслеживать новый вывод (как `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Просмотреть логи с временными метками:

`docker compose logs {{[-t|--timestamps]}}`

- Просмотреть только последние `n` строк логов для каждого контейнера:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Просмотреть логи начиная с определённого времени:

`docker compose logs --since {{временная_метка}}`

- Просмотреть логи до определённого времени:

`docker compose logs --until {{временная_метка}}`

- Просмотреть логи нескольких конкретных сервисов:

`docker compose logs {{сервис1 сервис2 ...}}`
