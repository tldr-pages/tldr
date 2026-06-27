# Clear-History

> 删除 PowerShell 会话命令历史记录中的条目。
> 注意：`clhy` 可以作为 `Clear-History` 的别名使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/clear-history>。

- 清除当前会话中的所有命令历史记录：

`Clear-History`

- 按指定名称清除命令：

`Clear-History -CommandLine "{{命令}}"`

- 按名称清除多个命令：

`Clear-History -CommandLine {{"命令1", "命令2", ...}}`

- 按 ID 清除指定历史记录条目：

`Clear-History -Id {{ID_编号}}`

- 清除多个 ID：

`Clear-History -Id {{id1, id2, ...}}`

- 清除 ID 范围内的命令：

`Clear-History -Id ({{起始_ID}}..{{结束_ID}})`

- 显示将被删除的内容：

`Clear-History -WhatIf`

- 清除前请求确认：

`Clear-History -Confirm`
