# mvn

> Maven.  
> Tool for building and managing Java-based projects.

- Compile a project:

`mvn compile`

- Delete the `target` folder, which contains all build outputs:

`mvn clean`

- Compile and build release package:

`mvn package`

- Compile and build release package, skipping unit tests:

`mvn package -Dmaven.test.skip=true`

- Install the built package in local maven repository:

`mvn install`

- Run a class with a main method:

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{arg1 arg2}}"`
