# ed

> 原始的 Unix 文本编辑器。
> 另见：`awk`，`sed`。
> 更多信息：<https://www.gnu.org/software/ed/manual/ed_manual.html>。

- 启动一个交互式编辑器会话，创建一个空文档：

`ed`

- 启动一个交互式编辑器会话，创建一个空文档并指定 [p]rompt：

`ed -p '> '`

- 启动一个交互式编辑器会话，创建一个空文档，并且不显示诊断信息、字节计数和 '!' 提示：

`ed -s`

- 编辑一个特定文件（这将显示加载文件的字节计数）：

`ed {{path/to/file}}`

- 用特定替换字符串替换所有行中的某个字符串：

`,s/{{regular_expression}}/{{replacement}}/g`