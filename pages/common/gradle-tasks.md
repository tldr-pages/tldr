# gradle tasks

> List available tasks in a Gradle project.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_tasks>.

- List the main tasks:

`gradle tasks`

- List all tasks including subtasks:

`gradle tasks --all`

- List tasks in a specific group:

`gradle tasks --group {{group_name}}`

- List tasks for a specific subproject:

`gradle :{{subproject}}:tasks`
