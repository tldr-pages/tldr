# gradle properties

> Display the properties of a Gradle project.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_properties>.

- Display all project properties:

`gradle properties`

- Display properties with detailed output:

`gradle properties {{[-i|--info]}}`

- Display properties for a specific subproject:

`gradle :{{subproject}}:properties`

- Display a specific property value:

`gradle properties | grep {{property_name}}`
