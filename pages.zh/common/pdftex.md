# pdftex

> 从 TeX 源文件编译 PDF 文档。
> 更多信息：<https://www.tug.org/applications/pdftex/>。

- 编译 PDF 文档：

`pdftex {{source.tex}}`

- 编译 PDF 文档，指定输出目录：

`pdftex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译 PDF 文档，在每个错误时退出：

`pdftex -halt-on-error {{source.tex}}`