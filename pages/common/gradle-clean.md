# gradle clean

> Delete the build directory and all generated files.
> More information: <https://docs.gradle.org/current/userguide/command_line_interface.html#cleaning_outputs>.

- Clean the build directory:

`gradle clean`

- Clean and then build the project:

`gradle clean build`

- Clean a specific subproject in a multi-project build:

`gradle :{{subproject}}:clean`

- Clean with more detailed logging:

`gradle clean {{[-i|--info]}}`
