# lualatex

> 使用 Lua 语言扩展的 TeX 版本，用于编译。
> 更多信息：<https://manned.org/lualatex.1>.

- 启动 `texlua` 作为 Lua 解释器运行：

`lualatex`

- 编译一个 TeX 文件为 PDF：

`lualatex {{path/to/file.tex}}`

- 无中断编译一个 TeX 文件（即使遇到错误也会继续）：

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- 编译一个 TeX 文件并指定输出文件名：

`lualatex -jobname={{filename}} {{path/to/file.tex}}`
