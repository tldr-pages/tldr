# carp

> Carp 的 REPL 和构建工具。
> 更多信息：<https://carp-lang.github.io/carp-docs/Manual.html>.

- 启动 REPL（交互式 shell）:

`carp`

- 以自定义提示符启动 REPL:

`carp --prompt "{{> }}"`

- 构建 `carp` 文件:

`carp -b {{path/to/file.carp}}`

- 构建并运行文件:

`carp -x {{path/to/file.carp}}`

- 启用优化构建文件:

`carp -b --optimize {{path/to/file.carp}}`

- 将文件转译为 C 代码:

`carp --generate-only {{path/to/file.carp}}`