# mvn compile

> Compile a Maven project's source code.
> More information: <https://maven.apache.org/plugins/maven-compiler-plugin/compile-mojo.html>.

- Compile the project's source code:

`mvn compile`

- Clean compiled files and recompile:

`mvn clean compile`

- Compile a specific module in a multi-module project:

`mvn compile {{[-pl|--projects]}} {{module_name}}`

- Skip tests while compiling:

`mvn compile {{[-D|--define]}} skipTests`
