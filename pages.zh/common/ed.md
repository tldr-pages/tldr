# ed

> 原始的 Unix 文本编辑器。
> 另见：`awk`，`sed`。
> 更多信息：<https://www.gnu.org/software/ed/manual/ed_manual.html>。

- 启动一个交互式编辑器会话，文档为空：

`ed`

- 启动一个交互式编辑器会话，文档为空，并指定提示符：

`ed --prompt='> '`

- 启动一个交互式编辑器会话，显示用户友好的错误信息：

`ed --verbose`

- 启动一个交互式编辑器会话，文档为空，不显示诊断信息、字节计数和 '!' 提示符：

`ed --quiet`

- 启动一个交互式编辑器会话，当命令失败时不改变退出状态：

`ed --loose-exit-status`

- 编辑特定文件（这会显示加载文件的字节计数）：

`ed {{path/to/file}}`

- 用特定替换字符串替换所有行中的字符串：

`,s/{{regular_expression}}/{{replacement}}/g`