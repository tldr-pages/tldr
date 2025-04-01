# typst

> 编译 Typst 文件为 PDF。
> 注意：指定输出位置是可选的。
> 更多信息：<https://github.com/typst/typst>。

- 使用模板（例如：`@preview/charged-ieee`）在指定目录中初始化一个新的 Typst 项目：

`typst init "{{template}}" {{path/to/directory}}`

- 编译 Typst 文件：

`typst compile {{path/to/source.typ}} {{path/to/output.pdf}}`

- 监视 Typst 文件并在文件更改时重新编译：

`typst watch {{path/to/source.typ}} {{path/to/output.pdf}}`

- 列出系统和指定目录中所有可发现的字体：

`typst --font-path {{path/to/fonts_directory}} fonts`
