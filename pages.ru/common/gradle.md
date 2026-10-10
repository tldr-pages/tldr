# gradle

> Система автоматизации сборки с открытым исходным кодом.
> Больше информации: <https://manned.org/gradle>.

- Скомпилировать пакет:

`gradle build`

- Исключить задачу тестирования:

`gradle build {{[-x|--exclude-task]}} test`

- Запустить в автономном режиме, чтобы предотвратить доступ Gradle к сети во время сборки:

`gradle build --offline`

- Очистить каталог сборки:

`gradle clean`

- Собрать пакет Android (APK) в режиме релиза:

`gradle assembleRelease`

- Вывести список основных задач:

`gradle tasks`

- Вывести список всех задач:

`gradle tasks --all`
