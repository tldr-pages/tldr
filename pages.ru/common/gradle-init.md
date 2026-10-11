# gradle init

> Инициализировать новый проект Gradle в интерактивном режиме.
> Больше информации: <https://docs.gradle.org/current/userguide/build_init_plugin.html>.

- Инициализировать новый проект Gradle в интерактивном режиме:

`gradle init`

- Инициализировать проект конкретного типа:

`gradle init --type {{basic|java-application|java-library|...}}`

- Инициализировать проект с конкретным DSL:

`gradle init --dsl {{groovy|kotlin}}`

- Инициализировать проект с конкретным тестовым фреймворком:

`gradle init --test-framework {{junit-jupiter|testng|spock}}`

- Инициализировать проект без интерактивных запросов:

`gradle init --type {{java-application}} --dsl {{kotlin}} --test-framework {{junit-jupiter}}`
