# mvn

> Apache Maven: build and manage Java-based projects.
> More information: <https://manned.org/mvn>.

- Compile a project:

`mvn compile`

- Compile and package the compiled code in its distributable format, such as a `jar`:

`mvn package`

- Compile and package, skipping unit tests:

`mvn package {{[-D|--define]}} skipTests`

- Install the built package in local maven repository. (This will invoke the compile and package commands too):

`mvn install`

- Delete build artifacts from the target directory:

`mvn clean`

- Do a clean and then invoke the package phase:

`mvn clean package`

- Clean and then package the code with a given build profile:

`mvn clean {{[-P|--activate-profiles]}} {{profile}} package`

- Run a class with a main method:

`mvn exec:java {{[-D|--define]}} exec.mainClass="{{com.example.Main}}" {{[-D|--define]}} exec.args="{{argument1 argument2 ...}}"`
