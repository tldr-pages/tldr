# gradle

> Gradle is an open source build automation system.
> More information: <https://gradle.org>.

- Assemble outputs and run checks:

`gradle build`

- Exclude a specific task:

`gradle build -x {{task_name}}`

- Run in offline mode to prevent Gradle from accessing the network during the build process:

`gradle build --offline`

- Clear the output directory:

`gradle clean`

- Compile and Release package:

`gradle assembleRelease`
