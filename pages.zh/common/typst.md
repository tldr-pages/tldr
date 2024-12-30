# typst

> 将 Typst 文件编译为 PDF。
> 注意：指定输出位置是可选的。
> 更多信息：<https://github.com/typst/typst>。

- 在给定目录中使用模板初始化一个新的 Typst 项目（例如，`@preview/charged-ieee`）：

`typst init "{{template}}" {{path/to/directory}}`

- 编译一个 Typst 文件：

`typst compile {{path/to/source.typ}} {{path/to/output.pdf}}`

- 监视一个 Typst 文件并在更改时重新编译：

`typst watch {{path/to/source.typ}} {{path/to/output.pdf}}`

- 列出系统和给定目录中所有可发现的字体：

`typst --font-path {{path/to/fonts_directory}} fonts`