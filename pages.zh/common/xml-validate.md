# xml validate

> 验证 XML 文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 仅验证一个或多个 XML 文档是否格式正确：

`xml validate {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 使用文档类型定义 (DTD) 验证一个或多个 XML 文档：

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 使用 XML 模式定义 (XSD) 验证一个或多个 XML 文档：

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 使用 Relax NG 模式 (RNG) 验证一个或多个 XML 文档：

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- 显示帮助：

`xml validate --help`