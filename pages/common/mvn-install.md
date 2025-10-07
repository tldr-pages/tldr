# mvn install

> Install third-party Maven dependencies and build the project.
> More information: <https://maven.apache.org/guides/getting-started/index.html#How_do_I_create_a_JAR_and_install_it_in_my_local_repository.3F>.

- Compile, test, package, and install the project into the local repository:

`mvn install`

- Skip tests during installation:

`mvn install {{[-D|--define]}} skipTests`

- Force update of dependencies before installing:

`mvn install {{[-U|--update-snapshots]}}`

- Skip test compilation and execution:

`mvn install {{[-D|--define]}} maven.test.skip=true`
