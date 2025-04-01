# xml elements

> 提取 XML 文档中的元素并显示其结构。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>.

- 从 XML 文档中提取元素（生成 XPATH 表达式）:

`xml elements {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 从 XML 文档中提取元素及其属性:

`xml elements -a {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 从 XML 文档中提取元素及其属性和值:

`xml elements -v {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- 从 XML 文档中打印排序后的唯一元素以查看其结构:

`xml elements -u {{path/to/input.xml|URI}}`

- 从 XML 文档中打印深度不超过 3 的排序后的唯一元素:

`xml elements -d{{3}} {{path/to/input.xml|URI}}`

- 显示帮助:

`xml elements --help`
