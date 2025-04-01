# pdftex

> 从 TeX 源文件编译 PDF 文档。
> 更多信息：<https://www.tug.org/applications/pdftex/>.

- 编译 PDF 文档：

`pdftex {{source.tex}}`

- 指定输出目录编译 PDF 文档：

`pdftex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译 PDF 文档，每个错误时停止：

`pdftex -halt-on-error {{source.tex}}`
