# asciidoctor

> 将 AsciiDoc 文件转换为可发布的格式。
> 更多信息： <https://docs.asciidoctor.org>.

- 将特定的 `.adoc` 文件转换为 HTML（默认输出格式）：

`asciidoctor {{path/to/file.adoc}}`

- 将特定的 `.adoc` 文件转换为 HTML 并链接一个 CSS 样式表：

`asciidoctor -a stylesheet {{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- 将特定的 `.adoc` 文件转换为可嵌入的 HTML，移除所有除主体内容之外的部分：

`asciidoctor --embedded {{path/to/file.adoc}}`

- 使用 `asciidoctor-pdf` 库将特定的 `.adoc` 文件转换为 PDF：

`asciidoctor --backend {{pdf}} --require {{asciidoctor-pdf}} {{path/to/file.adoc}}`
