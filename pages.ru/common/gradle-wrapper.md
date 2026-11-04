# gradle wrapper

> Генерировать файлы обёртки Gradle для проекта.
> Больше информации: <https://docs.gradle.org/current/userguide/gradle_wrapper.html>.

- Сгенерировать обёртку с текущей версией Gradle:

`gradle wrapper`

- Сгенерировать обёртку с конкретной версией Gradle:

`gradle wrapper --gradle-version {{8.5}}`

- Сгенерировать обёртку с конкретным типом дистрибутива:

`gradle wrapper --distribution-type {{bin|all}}`

- Сгенерировать обёртку, используя конкретный URL дистрибутива:

`gradle wrapper --gradle-distribution-url {{url}}`
