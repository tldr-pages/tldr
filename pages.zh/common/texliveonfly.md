# texliveonfly

> 在编译 `.tex` 文件时下载缺失的 TeX Live 包。
> 更多信息：<https://ctan.org/pkg/texliveonfly>。

- 在编译时下载缺失的包：

`texliveonfly {{source.tex}}`

- 使用特定的编译器（默认为 `pdflatex`）：

`texliveonfly --compiler={{compiler}} {{source.tex}}`

- 使用自定义的 TeX Live `bin` 文件夹：

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}`