# gradle tasks

> Выводить список доступных задач в проекте Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_tasks>.

- Вывести список основных задач:

`gradle tasks`

- Вывести список всех задач, включая подзадачи:

`gradle tasks --all`

- Вывести список задач в конкретной группе:

`gradle tasks --group {{имя_группы}}`

- Вывести список задач конкретного подпроекта:

`gradle :{{подпроект}}:tasks`
