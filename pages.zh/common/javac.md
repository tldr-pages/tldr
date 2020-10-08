# javac

> Java 程序编译器.

- 编译一个 .java 文件:

`javac {{file.java}}`

- 编译多个 .java 文件:

`javac {{file1.java}} {{file2.java}} {{file3.java}}`

- 编译当前目录内所有 .java 文件:

`javac {{*.java}}`

- 编译一个 .java 文件并将生成的 class 字节码文件放入一个指定目录:

`javac -d {{path/to/some/directory}} {{file.java}}`
