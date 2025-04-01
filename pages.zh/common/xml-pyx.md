# xml pyx

> 将 XML 文档转换为 PYX (ESIS - ISO 8879) 格式。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 将 XML 文档转换为 PYX 格式：

`xml pyx {{path/to/input.xml|URI}} > {{path/to/output.pyx}}`

- 从标准输入流将 XML 文档转换为 PYX 格式：

`cat {{path/to/input.xml}} | xml pyx > {{path/to/output.pyx}}`

- 显示帮助：

`xml pyx --help`