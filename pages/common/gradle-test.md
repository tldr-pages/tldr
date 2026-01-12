# gradle test

> Run tests using Gradle.
> More information: <https://docs.gradle.org/current/userguide/java_testing.html>.

- Run all tests:

`gradle test`

- Run tests with detailed output:

`gradle test {{[-i|--info]}}`

- Run a specific test class:

`gradle test --tests {{class_name}}`

- Run tests matching a pattern:

`gradle test --tests "{{pattern}}"`

- Rerun tests even if up-to-date:

`gradle test --rerun`
