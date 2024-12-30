# latexmk

> 将 LaTeX 源文件编译成成品文档。
> 在需要时自动进行多次运行。
> 更多信息：<https://mg.readthedocs.io/latexmk.html>。

- 从每个源文件编译 DVI（设备无关文件）文档：

`latexmk`

- 从特定源文件编译 DVI 文档：

`latexmk {{path/to/source.tex}}`

- 编译 PDF 文档：

`latexmk -pdf {{path/to/source.tex}}`

- 在查看器中打开文档，并在源文件更改时持续更新：

`latexmk -pvc {{path/to/source.tex}}`

- 强制生成文档，即使存在错误：

`latexmk -f {{path/to/source.tex}}`

- 清理为特定 TEX 文件创建的临时 TEX 文件：

`latexmk -c {{path/to/source.tex}}`

- 清理当前目录中的所有临时 TEX 文件：

`latexmk -c`