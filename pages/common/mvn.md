# mvn

> Apache Maven: build and manage Java-based projects.
> More information: <https://maven.apache.org/guides/>.

- Compile a project:

`mvn compile`

- Compile and package the project into a distributable format (such as a JAR):

`mvn package`

- Compile and package the project while skipping unit tests:

`mvn package -DskipTests`

- Install the built package into the local Maven repository (also runs compile and package):

`mvn install`

- Remove build artifacts from the `target` directory:

`mvn clean`

- Clean the project and then run the package phase:

`mvn clean package`

- Clean and package the project using a specific build profile:

`mvn clean -P {{profile}} package`

- Run a class with a `main` method using the Exec plugin:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{argument1 argument2 ...}}"`
