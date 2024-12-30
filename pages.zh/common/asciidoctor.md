# asciidoctor

> 将AsciiDoc文件转换为可发布的格式。
> 更多信息：<https://docs.asciidoctor.org>。

- 将特定的`.adoc`文件转换为HTML（默认输出格式）：

`asciidoctor {{path/to/file.adoc}}`

- 将特定的`.adoc`文件转换为HTML并链接CSS样式表：

`asciidoctor -a stylesheet {{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- 将特定的`.adoc`文件转换为可嵌入的HTML，去掉除主体以外的所有内容：

`asciidoctor --embedded {{path/to/file.adoc}}`

- 使用`asciidoctor-pdf`库将特定的`.adoc`文件转换为PDF：

`asciidoctor --backend {{pdf}} --require {{asciidoctor-pdf}} {{path/to/file.adoc}}`