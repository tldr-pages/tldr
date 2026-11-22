# zapier

> Создавать, автоматизировать интеграции Zapier и управлять ими.
> Некоторые подкоманды, такие как `build`, `init`, `scaffold`, `push`, `test` и другие, имеют собственную документацию.
> Больше информации: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md>.

- Подключиться к учётной записи Zapier:

`zapier login`

- Инициализировать новую интеграцию Zapier с шаблоном проекта:

`zapier init {{путь/к/каталогу}}`

- Добавить начальный триггер, действие создания, поиска или ресурс в интеграцию:

`zapier scaffold {{trigger|create|search|resource}} {{имя}}`

- Протестировать интеграцию:

`zapier test`

- Собрать и загрузить интеграцию в Zapier:

`zapier push`

- Показать справку:

`zapier help`

- Показать справку по конкретной команде:

`zapier help {{команда}}`
