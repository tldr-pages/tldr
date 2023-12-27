# javac

> Java application compiler.
> More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- Compile a `.java` file:

`javac {{path/to/file.java}}`

- Compile several `.java` files:

`javac {{path/to/file1.java}} {{path/to/file2.java}} {{path/to/file3.java}}`

- Compile all `.java` files in current directory:

`javac {{*.java}}`

- Compile a `.java` file and place the resulting class file in a specific directory:

`javac -d {{path/to/directory}} {{path/to/file.java}}`
