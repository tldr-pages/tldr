# docker system

> Управлять данными Docker и отображать общесистемную информацию.
> Больше информации: <https://docs.docker.com/reference/cli/docker/system/>.

- Показать использование диска Docker:

`docker system df`

- Показать подробную информацию об использовании диска:

`docker system df {{[-v|--verbose]}}`

- Удалить неиспользуемые данные (добавить `--volumes` для удаления неиспользуемых томов):

`docker system prune`

- Удалить неиспользуемые данные, созданные более указанного времени назад:

`docker system prune --filter "until={{часы}}h{{минуты}}m"`

- Удалить все неиспользуемые данные:

`docker system prune {{[-a|--all]}} --volumes`

- Показать события от демона Docker в реальном времени:

`docker system events`

- Показать события от контейнеров в реальном времени в формате JSON Lines:

`docker system events {{[-f|--filter]}} 'type=container' --format '{{json .}}'`

- Показать общесистемную информацию:

`docker system info`
