# XML格式

> 格式化XML文档。
> 更多信息：<https://xmlstar.sourceforge.net/docs.php>。

- 格式化XML文档，使用制表符缩进：

`xml format --indent-tab {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- 格式化HTML文档，使用4个空格缩进：

`xml format --html --indent-spaces {{4}} {{path/to/input.html|URI}} > {{path/to/output.html}}`

- 恢复格式不正确的XML文档中的可解析部分，不进行缩进：

`xml format --recover --noindent {{path/to/malformed.xml|URI}} > {{path/to/recovered.xml}}`

- 从`stdin`格式化XML文档，移除`DOCTYPE`声明：

`cat {{path\to\input.xml}} | xml format --dropdtd > {{path/to/output.xml}}`

- 格式化XML文档，省略XML声明：

`xml format --omit-decl {{path\to\input.xml|URI}} > {{path/to/output.xml}}`

- 显示帮助信息：

`xml format --help`