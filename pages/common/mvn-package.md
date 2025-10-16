# mvn package

> Package the compiled code of a Maven project into its distributable format (such as a JAR or WAR).
> More information: <https://manned.org/mvn>.

- Package a project:

`mvn package`

- Package a project while skipping test execution:

`mvn package {{[-D|--define]}} skipTests`

- Package a project and force Maven to update all dependencies:

`mvn package {{[-U|--update-snapshots]}}`
