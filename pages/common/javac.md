# javac

> Java Application Compiler.

- Compile a .java file:

`javac {{filename.java}}`

- Compile several .java files:

`javac {{filename1.java}} {{filename2.java}} {{filename3.java}}`

- Compile all .java files in current directory:

`javac {{*.java}}`

- Compile a .java file and place the resulting class file in a specific directory:

`javac -d {{path/to/some/directory}} {{filename.java}}`
