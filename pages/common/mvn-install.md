# mvn install

> Install third-party Maven dependencies and build the project.
> More information: <https://manned.org/mvn>.

- Compile, test, package, and install the project into the local repository:

`mvn install`

- Skip tests during installation:

`mvn install {{[-D|--define]}} skipTests`

- Force update of dependencies before installing:

`mvn install {{[-U|--update-snapshots]}}`

- Skip test compilation and execution:

`mvn install {{[-D|--define]}} maven.test.skip=true`
