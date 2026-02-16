# uv version

> Читать или обновлять версию проекта.
> Больше информации: <https://docs.astral.sh/uv/reference/cli/#uv-version>.

- Показать текущую версию проекта:

`uv version`

- Установить определённую версию проекта:

`uv version {{1.2.3}}`

- Увеличить версию проекта по семантическому версионированию:

`uv version --bump {{major|minor|patch}}`

- Предварительно просмотреть изменение версии без записи в `pyproject.toml`:

`uv version --bump {{patch}} --dry-run`

- Обновить версию определённого пакета в рабочем пространстве:

`uv version --package {{имя_пакета}} {{1.2.3}}`

- Показать версию в формате JSON:

`uv version --output-format json`
