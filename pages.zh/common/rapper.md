# rapper

> Raptor RDF 解析工具。
> Raptor RDF 语法库的一部分。
> 更多信息：<https://librdf.org/raptor/rapper.html>。

- 将 RDF/XML 文档转换为 Turtle：

`rapper -i rdfxml -o turtle {{path/to/file}}`

- 计算 Turtle 文件中的三元组数量：

`rapper -i turtle -c {{path/to/file}}`