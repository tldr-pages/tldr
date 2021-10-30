# javadoc

> 从源代码以 HTML 格式生成 Java API 文档。
> 更多信息：<https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>.

- 生成 Java 源代码的文档并将结果保存在文件夹中：

`javadoc -d {{path/to/directory/}} {{path/to/java_source_code}}`

- 生成指定编码的文档：

`javadoc -docencoding {{UTF-8}} {{path/to/java_source_code}}`

- 生成文档时，排除掉某些软件包：

`javadoc -exclude {{package_list}} {{path/to/java_source_code}}`
