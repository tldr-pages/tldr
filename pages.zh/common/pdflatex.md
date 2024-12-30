# pdflatex

> 从 LaTeX 源文件编译 PDF 文档。
> 更多信息：<https://manned.org/pdflatex>。

- 编译 PDF 文档：

`pdflatex {{source.tex}}`

- 编译 PDF 文档并指定输出目录：

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译 PDF 文档，在每个错误时退出：

`pdflatex -halt-on-error {{source.tex}}`