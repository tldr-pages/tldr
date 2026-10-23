# zapier scaffold

> Добавлять начальный триггер, действие создания, поиска или ресурс в интеграцию.
> Больше информации: <https://platform.zapier.com/reference/cli#scaffold>.

- Сгенерировать новый триггер, действие создания, поиска или ресурс:

`zapier scaffold {{trigger|search|create|resource}} {{существительное}}`

- Указать пользовательский каталог назначения для сгенерированных файлов:

`zapier scaffold {{trigger|search|create|resource}} {{существительное}} {{[-d|--dest]}}={{путь/к/каталогу}}`

- Перезаписать существующие файлы при генерации:

`zapier scaffold {{trigger|search|create|resource}} {{существительное}} {{[-f|--force]}}`

- Исключить комментарии из сгенерированных файлов:

`zapier scaffold {{trigger|search|create|resource}} {{существительное}} --no-help`

- Показать дополнительную отладочную информацию:

`zapier scaffold {{[-d|--debug]}}`
