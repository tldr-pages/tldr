# docker container stop

> Останавливать один или несколько запущенных контейнеров.
> Больше информации: <https://docs.docker.com/reference/cli/docker/container/stop/>.

- Остановить контейнер Docker:

`docker {{[stop|container stop]}} {{контейнер}}`

- Остановить контейнер, отправив определённый сигнал:

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{сигнал}} {{контейнер}}`

- Остановить контейнер, ожидая указанное количество секунд перед принудительным завершением:

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{секунды}} {{контейнер}}`

- Остановить один или несколько контейнеров:

`docker {{[stop|container stop]}} {{контейнер1 контейнер2 ...}}`

- Показать справку:

`docker {{[stop|container stop]}} --help`
