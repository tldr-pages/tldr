# xsltproc

> 使用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML）。
> 更多信息：<http://www.xmlsoft.org/xslt/xsltproc.html>。

- 使用特定的 XSLT 样式表转换 XML 文件：

`xsltproc --output {{path/to/output_file.html}} {{path/to/stylesheet_file.xslt}} {{path/to/file.xml}}`

- 向样式表中的参数传递值：

`xsltproc --output {{path/to/output_file.html}} --stringparam "{{name}}" "{{value}}" {{path/to/stylesheet_file.xslt}} {{path/to/xml_file.xml}}`