# jar

> Java 应用程序/库打包工具。
> 更多信息：<https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>。

- 将当前目录中的所有文件递归归档到 .jar 文件中：

`jar cf {{file.jar}} *`

- 将 .jar/.war 文件解压到当前目录：

`jar -xvf {{file.jar}}`

- 列出 .jar/.war 文件的内容：

`jar tf {{path/to/file.jar}}`

- 以详细输出列出 .jar/.war 文件的内容：

`jar tvf {{path/to/file.jar}}`