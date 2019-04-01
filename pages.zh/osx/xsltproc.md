# xsltproc

> 用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML ）.

- 使用特定的 XSLT 样式表转换 XML 文件:

`xsltproc --output {{输出.html}} {{样式表.xslt}} {{xml文件.xml}}`

- 将值传递给样式表中的参数:

`xsltproc --output {{输出.html}} --stringparam {{键名}} {{值}} {{样式表.xslt}} {{xml文件.xml}}`
