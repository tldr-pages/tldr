# latex

> 从 LaTeX 源文件编译 DVI 文档。
> 更多信息：<https://www.latex-project.org>.

- 编译 DVI 文档：

`latex {{source.tex}}`

- 指定输出目录编译 DVI 文档：

`latex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译 DVI 文档，遇到错误时停止：

`latex -halt-on-error {{source.tex}}`