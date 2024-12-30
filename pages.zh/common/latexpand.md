# latexpand

> 通过删除注释和解析 `\include`、`\input` 等简化 LaTeX 源文件。
> 更多信息：<https://www.ctan.org/pkg/latexpand>。

- 简化指定的源文件并将结果保存到指定的 [o]utput 文件：

`latexpand --output {{path/to/output.tex}} {{path/to/file.tex}}`

- 不删除注释：

`latexpand --keep-comments --output {{path/to/output.tex}} {{path/to/file.tex}}`

- 不扩展 `\include`、`\input` 等：

`latexpand --keep-includes --output {{path/to/output.tex}} {{path/to/file.tex}}`

- 尽可能扩展 `\usepackage`，只要相应的 STY 文件可以找到：

`latexpand --expand-usepackage --output {{path/to/output.tex}} {{path/to/file.tex}}`

- 内联指定的 BBL 文件：

`latexpand --expand-bbl {{path/to/bibliography.bbl}} --output {{path/to/output.tex}} {{path/to/file.tex}}`