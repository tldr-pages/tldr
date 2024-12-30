# javadoc

> 从源代码生成 HTML 格式的 Java API 文档。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javadoc.html>。

- 为 Java 源代码生成文档并将结果保存到目录中：

`javadoc -d {{path/to/directory/}} {{path/to/java_source_code}}`

- 使用特定编码生成文档：

`javadoc -docencoding {{UTF-8}} {{path/to/java_source_code}}`

- 生成文档时排除某些包：

`javadoc -exclude {{package_list}} {{path/to/java_source_code}}`