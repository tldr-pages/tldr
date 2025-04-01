# lpmove

> 将作业或所有作业移动到另一个打印机。
> 参见：`cancel`, `lp`, `lpr`, `lprm`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpmove.html>。

- 将特定作业移动到 `new_printer`：

`lpmove {{job_id}} {{new_printer}}`

- 将来自 `old_printer` 的作业移动到 `new_printer`：

`lpmove {{old_printer}}-{{job_id}} {{new_printer}}`

- 将 `old_printer` 上的所有作业移动到 `new_printer`：

`lpmove {{old_printer}} {{new_printer}}`

- 将特定服务器上的特定作业移动到 `new_printer`：

`lpmove -h {{server}} {{job_id}} {{new_printer}}`
