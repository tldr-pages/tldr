# gradle test

> Запускать тесты с помощью Gradle.
> Больше информации: <https://docs.gradle.org/current/userguide/java_testing.html>.

- Запустить все тесты:

`gradle test`

- Запустить тесты с подробным выводом:

`gradle test {{[-i|--info]}}`

- Запустить конкретный тестовый класс:

`gradle test --tests {{имя_класса}}`

- Запустить тесты, соответствующие шаблону:

`gradle test --tests "{{шаблон}}"`

- Перезапустить тесты, даже если они актуальны:

`gradle test --rerun`
