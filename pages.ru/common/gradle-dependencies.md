# gradle dependencies

> Отображать дерево зависимостей для проекта Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_dependencies>.

- Показать все зависимости:

`gradle dependencies`

- Показать зависимости для конкретной конфигурации:

`gradle dependencies --configuration {{implementation}}`

- Показать зависимости для конкретного подпроекта:

`gradle :{{подпроект}}:dependencies`

- Показать зависимости и сохранить в файл:

`gradle dependencies > {{путь/к/зависимостям.txt}}`
