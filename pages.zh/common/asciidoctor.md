# asciidoctor

> 将 AsciiDoc 文件转换为可发布的格式。
> 更多信息：<https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>。

- 将特定 `.adoc` 文件转换为 HTML（默认输出格式）：

`asciidoctor {{路径/到/file.adoc}}`

- 将特定 `.adoc` 文件转换为 HTML 并链接 CSS 样式表：

`asciidoctor {{[-a|--attribute]}} stylesheet={{路径/到/stylesheet.css}} {{路径/到/file.adoc}}`

- 将特定 `.adoc` 文件转换为嵌入式 HTML，移除正文以外的所有内容：

`asciidoctor {{[-e|--embedded]}} {{路径/到/file.adoc}}`

- 使用 `asciidoctor-pdf` 库将特定 `.adoc` 文件转换为 PDF：

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{路径/到/file.adoc}}`
