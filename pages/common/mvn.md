# mvn

> Apache Maven.
> Tool for building and managing Java-based projects.
> More information: <https://maven.apache.org>.

- Compile a project:

`mvn compile`

- Compile and package the compiled code in its distributable format, such as a `jar`:

`mvn package`

- Compile and package, skipping unit tests:

`mvn package -Dmaven.test.skip=true`

- Install the built package in local maven repository. (This will invoke the compile and package commands too):

`mvn install`

- Delete build artifacts from the target directory:

`mvn clean`

- Do a clean and then invoke the package phase:

`mvn clean package`

- Clean and then package the code with a given build profile:

`mvn clean -P{{profile}} package`

- Run a class with a main method:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{arg1 arg2}}"`
