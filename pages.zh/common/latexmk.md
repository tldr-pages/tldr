# latexmk

> 编译 LaTeX 源文件以生成最终文档。
> 在需要时自动进行多次编译。
> 更多信息：<https://mg.readthedocs.io/latexmk.html>.

- 从所有源文件编译 DVI（与设备无关的文件）文档：

`latexmk`

- 从特定源文件编译 DVI 文档：

`latexmk {{path/to/source.tex}}`

- 编译 PDF 文档：

`latexmk -pdf {{path/to/source.tex}}`

- 在查看器中打开文档，并在源文件更改时连续更新：

`latexmk -pvc {{path/to/source.tex}}`

- 即使有错误也要强制生成文档：

`latexmk -f {{path/to/source.tex}}`

- 清理为特定 TEX 文件创建的临时 TEX 文件：

`latexmk -c {{path/to/source.tex}}`

- 清理当前目录中的所有临时 TEX 文件：

`latexmk -c`
