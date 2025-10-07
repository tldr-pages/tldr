# mvn install

> Install third-party Maven dependencies and build the project.
> More information: <https://maven.apache.org/guides/getting-started/index.html#How_do_I_create_a_JAR_and_install_it_in_my_local_repository.3F>.

- Compile, test, package, and install the project into the local repository:

`mvn install`

- Skip tests during installation:

`mvn install -DskipTests`

- Force update of dependencies before installing:

`mvn install -U`

- Skip test compilation and execution:

`mvn install -Dmaven.test.skip=true`
