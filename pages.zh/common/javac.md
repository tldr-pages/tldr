# javac

> Java 程序编译器。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- 编译一个 `.java` 文件：

`javac {{文件名.java}}`

- 编译多个 `.java` 文件：

`javac {{文件名1.java}} {{文件名2.java}} {{文件名3.java}}`

- 编译当前目录内所有 `.java` 文件：

`javac {{*.java}}`

- 编译一个 `.java` 文件并将生成的 class 字节码文件放入一个指定目录：

`javac -d {{路径/到/目录}} {{文件名.java}}`
