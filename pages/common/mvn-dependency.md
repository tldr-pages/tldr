# mvn dependency

> Manage and analyze Maven project dependencies.
> Provides goals for viewing, resolving, and copying project dependencies.
> More information: <https://maven.apache.org/plugins/maven-dependency-plugin/usage.html>.

- Display the full dependency tree, including direct and transitive dependencies:

`mvn dependency:tree`

- Analyze the dependencies and highlight unused or undeclared ones:

`mvn dependency:analyze`

- Copy all project dependencies (by default, to `target/dependency/`):

`mvn dependency:copy-dependencies`

- Resolve and download all project dependencies to the local Maven repository:

`mvn dependency:resolve`

- Force Maven to update all dependencies from remote repositories:

`mvn dependency:resolve {{[-U|--update-snapshots]}}`
