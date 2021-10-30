# jar

> Java 应用程序 / 类库打包程序。
> 更多信息：<https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- 将当前目录中的所有文件递归归档到 `.jar` 文件中：

`jar cf {{file.jar}} *`

- 将 `.jar` / `.war` 文件解压缩到当前目录：

`jar -xvf {{file.jar}}`

- 列出 `.jar` / `.war` 文件内容：

`jar tf {{path/to/file.jar}}`

- 列出带有详细输出的 `.jar` / `.war` 文件内容：

`jar tvf {{path/to/file.jar}}`
