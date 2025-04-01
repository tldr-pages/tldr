# xml transform

> 使用 XSLT 转换 XML 文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>.

- 使用 XSL 样式表转换 XML 文档，并传递一个 XPATH 参数和一个文本字符串参数：

`xml transform {{path/to/stylesheet.xsl}} -p "{{Count='count(/xml/table/rec)'}}" -s {{Text="Count="}} {{path/to/input.xml|URI}}`

- 显示帮助信息：

`xml transform --help`
