# 获取别名

> 列出并获取当前 PowerShell 会话中的命令别名。
> 此命令只能在 PowerShell 中运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>。

- 列出当前会话中的所有别名：

`Get-Alias`

- 获取别名命令名称：

`Get-Alias {{command_alias}}`

- 列出分配给特定命令的所有别名：

`Get-Alias -Definition {{command}}`

- 列出以 `abc` 开头的别名，排除以 `def` 结尾的别名：

`Get-Alias {{abc}}* -Exclude *{{def}}`