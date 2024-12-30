# XML 验证

> 验证 XML 文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 仅验证一个或多个 XML 文档的格式正确性：

`xml validate {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 验证一个或多个 XML 文档是否符合文档类型定义 (DTD)：

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 验证一个或多个 XML 文档是否符合 XML 架构定义 (XSD)：

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 验证一个或多个 XML 文档是否符合 Relax NG 架构 (RNG)：

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 显示帮助信息：

`xml validate --help`