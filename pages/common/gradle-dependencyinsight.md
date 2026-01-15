# gradle dependencyInsight

> Display insight into a specific dependency in a Gradle project.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#reporting_dependencies>.

- Show insight for a specific dependency:

`gradle dependencyInsight --dependency {{package_name}}`

- Show insight for a dependency in a specific configuration:

`gradle dependencyInsight --dependency {{package_name}} --configuration {{configuration_name}}`

- Show insight for a specific subproject:

`gradle :{{subproject}}:dependencyInsight --dependency {{package_name}}`

- Show insight with the full dependency path:

`gradle dependencyInsight --dependency {{package_name}} {{[-i|--info]}}`
