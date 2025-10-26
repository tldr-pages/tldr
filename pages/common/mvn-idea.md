# mvn idea

> Generate IntelliJ IDEA project files (`.ipr`, `.iml`, and `.iws`) for a Maven project.
> This plugin is retired. It is no longer maintained.
> More information: <https://maven.apache.org/plugins/maven-idea-plugin/usage.html>.

- Generate all IntelliJ IDEA project files:

`mvn idea:idea`

- Generate only the project (`.ipr`) file:

`mvn idea:project`

- Generate only the workspace (`.iws`) file:

`mvn idea:workspace`

- Generate only module (`.iml`) files:

`mvn idea:module`

- Delete all generated project files:

`mvn idea:clean`
