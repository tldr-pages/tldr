# gradle clean

> Удалять каталог сборки и все сгенерированные файлы.
> Больше информации: <https://docs.gradle.org/current/userguide/command_line_interface.html#cleaning_outputs>.

- Очистить каталог сборки:

`gradle clean`

- Очистить и затем собрать проект:

`gradle clean build`

- Очистить конкретный подпроект в многопроектной сборке:

`gradle :{{подпроект}}:clean`

- Очистить с более подробным логированием:

`gradle clean {{[-i|--info]}}`
