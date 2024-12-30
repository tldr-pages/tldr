# Carp

> Carp 的 REPL 和构建工具。
> 更多信息：<https://carp-lang.github.io/carp-docs/Manual.html>。

- 启动 REPL（交互式 shell）：

`carp`

- 启动带自定义提示符的 REPL：

`carp --prompt "{{> }}"`

- 构建一个 `carp` 文件：

`carp -b {{path/to/file.carp}}`

- 构建并运行一个文件：

`carp -x {{path/to/file.carp}}`

- 在启用优化的情况下构建一个文件：

`carp -b --optimize {{path/to/file.carp}}`

- 将一个文件转译为 C 代码：

`carp --generate-only {{path/to/file.carp}}`