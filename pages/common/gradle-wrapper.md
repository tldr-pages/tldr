# gradle wrapper

> Generate the Gradle wrapper files for a project.
> More information: <https://docs.gradle.org/current/userguide/gradle_wrapper.html>.

- Generate wrapper with the current Gradle version:

`gradle wrapper`

- Generate wrapper with a specific Gradle version:

`gradle wrapper --gradle-version {{8.5}}`

- Generate wrapper with a specific distribution type:

`gradle wrapper --distribution-type {{bin|all}}`

- Generate wrapper using a specific distribution URL:

`gradle wrapper --gradle-distribution-url {{url}}`
