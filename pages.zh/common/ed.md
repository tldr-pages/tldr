# ed

> 原始的 Unix 文本编辑器。
> 参见：`awk`，`sed`。
> 更多信息：<https://www.gnu.org/software/ed/manual/ed_manual.html>。

- 以空文档启动交互式编辑会话：

`ed`

- 以空文档启动交互式编辑会话并设置特定的提示符：

`ed {{[-p|--prompt]}} '{{> }}'`

- 以用户友好的错误信息启动交互式编辑会话：

`ed {{[-v|--verbose]}}`

- 以空文档启动交互式编辑会话，不显示诊断信息、字节计数和 '!' 提示符：

`ed {{[-q|--quiet]}} {{[-s|--script]}}`

- 启动交互式编辑会话，当命令失败时不会更改退出状态：

`ed {{[-l|--loose-exit-status]}}`

- 编辑特定文件（显示加载文件的字节计数）：

`ed {{path/to/file}}`

- 替换所有行中的字符串为特定替换字符串：

`,s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 退出 `ed`：

`q<Enter>`
