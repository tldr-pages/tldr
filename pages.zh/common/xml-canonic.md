# XML 规范化

> 使 XML 文档规范化。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 使 XML 文档规范化，保留注释：

`xml canonic {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 使 XML 文档规范化，删除注释：

`xml canonic --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 使用文件中的 XPATH，使 XML 专门规范化，保留注释：

`xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- 显示帮助信息：

`xml canonic --help`