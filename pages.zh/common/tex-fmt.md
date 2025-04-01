# tex-fmt

> 格式化 LaTeX 源代码。
> 更多信息：<https://github.com/WGUNDERWOOD/tex-fmt>。

- 格式化一个文件并覆盖原文件：

`tex-fmt {{path/to/file.tex}}`

- 检查文件是否已正确格式化：

`tex-fmt --check {{path/to/file.tex}}`

- 从 `stdin` 读取文件并格式化，输出到 `stdout`：

`cat {{path/to/file.tex}} | tex-fmt --stdin`
