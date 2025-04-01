# pdflatex

> 从 LaTeX 源文件编译生成 PDF 文档。
> 更多信息：<https://manned.org/pdflatex>.

- 编译生成 PDF 文档：

`pdflatex {{source.tex}}`

- 指定输出目录编译生成 PDF 文档：

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译生成 PDF 文档，遇到错误时停止：

`pdflatex -halt-on-error {{source.tex}}`