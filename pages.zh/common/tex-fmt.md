# tex-fmt

> 格式化 LaTeX 源代码。
> 更多信息：<https://github.com/WGUNDERWOOD/tex-fmt>。

- 格式化一个文件，覆盖原文件：

`tex-fmt {{path/to/file.tex}}`

- 检查一个文件是否格式正确：

`tex-fmt --check {{path/to/file.tex}}`

- 格式化从 `stdin` 读取的文件并输出到 `stdout`：

`cat {{path/to/file.tex}} | tex-fmt --stdin`