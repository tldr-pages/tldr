# tex

> 从 TeX 源文件编译生成 DVI 文档。
> 更多信息：<https://www.tug.org/begin.html>.

- 编译生成 DVI 文档：

`tex {{source.tex}}`

- 编译生成 DVI 文档，并指定输出目录：

`tex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译生成 DVI 文档，每次遇到错误时退出：

`tex -halt-on-error {{source.tex}}`
