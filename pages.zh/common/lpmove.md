# lpmove

> 将一个作业或所有作业移动到另一台打印机。
> 另见：`cancel`，`lp`，`lpr`，`lprm`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpmove.html>。

- 将特定作业移动到 `new_printer`：

`lpmove {{job_id}} {{new_printer}}`

- 将作业从 `old_printer` 移动到 `new_printer`：

`lpmove {{old_printer}}-{{job_id}} {{new_printer}}`

- 将所有作业从 `old_printer` 移动到 `new_printer`：

`lpmove {{old_printer}} {{new_printer}}`

- 将特定作业移动到特定服务器上的 `new_printer`：

`lpmove -h {{server}} {{job_id}} {{new_printer}}`