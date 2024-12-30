# javac

> Java 应用程序编译器。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>。

- 编译一个 `.java` 文件：

`javac {{path/to/file.java}}`

- 编译多个 `.java` 文件：

`javac {{path/to/file1.java path/to/file2.java ...}}`

- 编译当前目录中的所有 `.java` 文件：

`javac {{*.java}}`

- 编译一个 `.java` 文件并将生成的类文件放入指定目录：

`javac -d {{path/to/directory}} {{path/to/file.java}}`