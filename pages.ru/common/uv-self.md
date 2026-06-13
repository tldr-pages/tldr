# uv self

> Управлять исполняемым файлом `uv`.
> Больше информации: <https://docs.astral.sh/uv/reference/cli/#uv-self>.

- Обновить `uv` до последней версии:

`uv self update`

- Обновить `uv` до определённой версии:

`uv self update {{0.4.0}}`

- Проверить наличие обновлений `uv` без установки:

`uv self update --dry-run`

- Обновить `uv` с подробным выводом:

`uv self update {{[-v|--verbose]}}`

- Показать текущую версию `uv`:

`uv self version`

- Показать только номер версии:

`uv self version --short`

- Показать информацию о версии в формате JSON:

`uv self version --output-format json`
