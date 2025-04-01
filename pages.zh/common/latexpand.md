# latexpand

> 通过移除注释和解析 `\include`、`\input` 等命令来简化 LaTeX 源文件。
> 更多信息：<https://www.ctan.org/pkg/latexpand>.

- 简化指定的源文件，并将结果保存到指定的输出文件：

`latexpand {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- 不移除注释：

`latexpand --keep-comments {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- 不展开 `\include`、`\input` 等命令：

`latexpand --keep-includes {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- 尽可能地展开 `\usepackage` 命令，直到找到相应的 STY 文件：

`latexpand --expand-usepackage {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`

- 内联指定的 BBL 文件：

`latexpand --expand-bbl {{path/to/bibliography.bbl}} {{[-o|--output]}} {{path/to/output.tex}} {{path/to/file.tex}}`