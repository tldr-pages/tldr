# gradle dependencies

> Display the dependency tree for a Gradle project.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_dependencies>.

- Display all dependencies:

`gradle dependencies`

- Display dependencies for a specific configuration:

`gradle dependencies --configuration {{implementation}}`

- Display dependencies for a specific subproject:

`gradle :{{subproject}}:dependencies`

- Display dependencies and save to a file:

`gradle dependencies > {{path/to/dependencies.txt}}`
