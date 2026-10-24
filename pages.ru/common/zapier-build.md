# zapier build

> Собирать готовый к загрузке `zip`-архив интеграции Zapier.
> Больше информации: <https://platform.zapier.com/reference/cli#build>.

- Создать сборку:

`zapier build`

- Отключить автоматическое определение зависимостей (будут включены только файлы, необходимые для `index.js`):

`zapier build --disable-dependency-detection`

- Показать дополнительную отладочную информацию:

`zapier build {{[-d|--debug]}}`
