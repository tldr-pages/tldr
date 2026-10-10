# gradle properties

> Отображать свойства проекта Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_properties>.

- Показать все свойства проекта:

`gradle properties`

- Показать свойства с подробным выводом:

`gradle properties {{[-i|--info]}}`

- Показать свойства конкретного подпроекта:

`gradle :{{подпроект}}:properties`

- Показать значение конкретного свойства:

`gradle properties | grep {{имя_свойства}}`
