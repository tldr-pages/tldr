# XML 元素

> 提取元素并显示 XML 文档的结构。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 从 XML 文档中提取元素（生成 XPATH 表达式）：

`xml elements {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 从 XML 文档中提取元素及其属性：

`xml elements -a {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 从 XML 文档中提取元素及其属性和数值：

`xml elements -v {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 打印从 XML 文档中排序后的唯一元素，以查看其结构：

`xml elements -u {{path/to/input.xml|URI}}`

- 打印从 XML 文档中排序后的唯一元素，深度限制为 3：

`xml elements -d{{3}} {{path/to/input.xml|URI}}`

- 显示帮助信息：

`xml elements --help`