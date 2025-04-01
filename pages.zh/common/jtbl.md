# jtbl

> 用于在终端中将 JSON 和 JSON Lines 数据打印为表格的工具。
> 更多信息：<https://github.com/kellyjonbrazil/jtbl>.

- 从 JSON 或 JSON Lines 输入中打印表格：

`cat {{文件.json}} | jtbl`

- 打印表格并指定用于换行的列宽：

`cat {{文件.json}} | jtbl --cols={{宽度}}`

- 打印表格并截断行而不是换行：

`cat {{文件.json}} | jtbl -t`

- 打印表格并不换行或截断行：

`cat {{文件.json}} | jtbl -n`
