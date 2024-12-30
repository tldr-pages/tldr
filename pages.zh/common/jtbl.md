# jtbl

> 用于在终端中将 JSON 和 JSON Lines 数据打印为表格的工具。
> 更多信息：<https://github.com/kellyjonbrazil/jtbl>。

- 从 JSON 或 JSON Lines 输入打印表格：

`cat {{file.json}} | jtbl`

- 打印表格并指定列宽以便换行：

`cat {{file.json}} | jtbl --cols={{width}}`

- 打印表格并截断行而不是换行：

`cat {{file.json}} | jtbl -t`

- 打印表格并且不换行或截断行：

`cat {{file.json}} | jtbl -n`