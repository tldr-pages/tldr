# gradle dependencyInsight

> Отображать подробную информацию о конкретной зависимости в проекте Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#reporting_dependencies>.

- Показать информацию о конкретной зависимости:

`gradle dependencyInsight --dependency {{имя_пакета}}`

- Показать информацию о зависимости в конкретной конфигурации:

`gradle dependencyInsight --dependency {{имя_пакета}} --configuration {{имя_конфигурации}}`

- Показать информацию для конкретного подпроекта:

`gradle :{{подпроект}}:dependencyInsight --dependency {{имя_пакета}}`

- Показать информацию с полным путём зависимости:

`gradle dependencyInsight --dependency {{имя_пакета}} {{[-i|--info]}}`
