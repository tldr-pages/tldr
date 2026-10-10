# gradle build

> Собирать проект с помощью Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#common_tasks>.

- Собрать проект:

`gradle build`

- Выполнить чистую сборку:

`gradle clean build`

- Собрать проект, пропуская тесты:

`gradle build {{[-x|--exclude-task]}} test`

- Собрать с более подробным логированием:

`gradle build {{[-i|--info]}}`
