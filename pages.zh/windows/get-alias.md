# Get-Alias

> 列出或获取当前 PowerShell 会话中的命令别名。
> 此命令只能在 PowerShell 中运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>。

- 列出当前会话中的所有别名：

`Get-Alias`

- 获取指定别名对应的命令名称：

`Get-Alias {{命令别名}}`

- 列出指定命令的所有别名：

`Get-Alias -Definition {{命令}}`

- 列出以 `abc` 开头的别名，排除以 `def` 结尾的别名：

`Get-Alias {{abc}}* -Exclude *{{def}}`
