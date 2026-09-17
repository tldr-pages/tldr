# gradle projects

> Display the sub-projects of a Gradle project.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_projects>.

- Display all sub-projects:

`gradle projects`

- Display sub-projects with their descriptions:

`gradle projects {{[-i|--info]}}`

- Display sub-projects of a specific project in a multi-project build:

`gradle :{{subproject}}:projects`
