# javac

> Java application compiler.
> More information: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/javac.html>.

- Compile a `.java` file:

`javac {{file.java}}`

- Compile several `.java` files:

`javac {{file1.java}} {{file2.java}} {{file3.java}}`

- Compile all `.java` files in current directory:

`javac {{*.java}}`

- Compile a `.java` file and place the resulting class file in a specific directory:

`javac -d {{path/to/directory}} {{file.java}}`
