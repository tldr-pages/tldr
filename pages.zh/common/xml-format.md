# xml format

> 格式化 XML 文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>.

- 格式化 XML 文档，使用制表符缩进：

`xml format --indent-tab {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 格式化 HTML 文档，使用 4 个空格缩进：

`xml format --html --indent-spaces {{4}} {{path/to/input.html|URI}} > {{path/to/output.html}}`

- 恢复损坏的 XML 文档的可解析部分，不缩进：

`xml format --recover --noindent {{path/to/malformed.xml|URI}} > {{path/to/recovered.xml}}`

- 从 `stdin` 格式化 XML 文档，移除 `DOCTYPE` 声明：

`cat {{path\to\input.xml}} | xml format --dropdtd > {{path/to/output.xml}}`

- 格式化 XML 文档，省略 XML 声明：

`xml format --omit-decl {{path\to\input.xml|URI}} > {{path/to/output.xml}}`

- 显示帮助：

`xml format --help`