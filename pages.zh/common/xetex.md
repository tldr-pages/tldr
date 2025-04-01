# xetex

> 从 XeTeX 源文件编译生成 PDF 文档。
> 更多信息：<https://www.tug.org/xetex/>.

- 编译生成 PDF 文档：

`xetex {{source.tex}}`

- 编译生成 PDF 文档，并指定输出目录：

`xetex -output-directory={{path/to/directory}} {{source.tex}}`

- 编译生成 PDF 文档，如果出现错误则退出：

`xetex -halt-on-error {{source.tex}}`
