# cmark

> 将 CommonMark Markdown 格式的文本转换为其他格式。
> 更多信息：<https://github.com/commonmark/cmark>。

- 将 CommonMark Markdown 文件渲染为 HTML：

`cmark --to html {{filename.md}}`

- 将 `stdin` 的数据转换为 LaTeX：

`cmark --to latex`

- 将直角引号转换为智能引号：

`cmark --smart --to html {{filename.md}}`

- 验证 UTF-8 字符：

`cmark --validate-utf8 {{filename.md}}`
