# Get-Alias

> 列出并获取当前 PowerShell 会话中的命令别名。
> 该命令只能在 PowerShell 下运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- 列出当前会话中的所有别名：

`Get-Alias`

- 获取别名对应的命令名称：

`Get-Alias {{command_alias}}`

- 列出分配给特定命令的所有别名：

`Get-Alias -Definition {{command}}`

- 列出以 `abc` 开头但不以 `def` 结尾的别名：

`Get-Alias {{abc}}* -Exclude *{{def}}`
