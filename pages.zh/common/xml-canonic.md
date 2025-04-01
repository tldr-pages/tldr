# xml canonic

> 将 XML 文档规范化。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>.

- 将 XML 文档规范化，保留注释：

`xml canonic {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 将 XML 文档规范化，移除注释：

`xml canonic --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 使用文件中的 XPATH 将 XML 独家规范化，保留注释：

`xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- 显示帮助：

`xml canonic --help`