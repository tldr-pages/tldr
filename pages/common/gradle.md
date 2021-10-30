# gradle

> Gradle is an open source build automation system.
> More information: <https://gradle.org>.

- Compile a package:

`gradle build`

- Exclude test task:

`gradle build -x {{test}}`

- Run in offline mode to prevent Gradle from accessing the network during builds:

`gradle build --offline`

- Clear the build directory:

`gradle clean`

- Build an Android Package (APK) in release mode:

`gradle assembleRelease`

- List the main tasks:

`gradle tasks`

- List all the tasks:

`gradle tasks --all`
