# mvn

> Apache Maven.
> Tool for building and managing Java-based projects.

- Compile and build release package:

`mvn package`

- Execute with debug information:

`mvn -X package`

- Use an alternative POM(Project Object Model):

`mvn -f {{path/to/custom_pom.xml}} compile`

- Invoke more that one Lifecycle phase with arguments:

`mvn clean -P {{a_profile}} package clean`

- Run a class with a main method:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{arg1 arg2}}"`
