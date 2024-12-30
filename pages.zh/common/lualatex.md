# lualatex

> 一种扩展版本的 TeX，使用 Lua 进行编译。
> 更多信息：<https://manned.org/lualatex.1>。

- 启动 `texlua` 作为 Lua 解释器：

`lualatex`

- 将 Tex 文件编译为 PDF：

`lualatex {{path/to/file.tex}}`

- 编译 Tex 文件而不发生错误中断：

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- 使用特定的输出文件名编译 Tex 文件：

`lualatex -jobname={{filename}} {{path/to/file.tex}}`