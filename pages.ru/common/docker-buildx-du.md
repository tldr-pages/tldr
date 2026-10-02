# docker buildx du

> Показывать использование диска для сборщика.
> Больше информации: <https://docs.docker.com/reference/cli/docker/buildx/du/>.

- Показать использование диска:

`docker buildx du`

- Отфильтровать вывод по определённому условию:

`docker buildx du --filter "{{description~=golang}}"`

- Показать подробный вывод:

`docker buildx du --verbose`

- Отформатировать вывод с использованием шаблона Go:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- Вывести в удобочитаемом формате JSON с использованием команды `jq`:

`docker buildx du --format json | jq .`

- Показать использование диска для определённого сборщика:

`docker buildx du --builder {{имя_сборщика}}`
