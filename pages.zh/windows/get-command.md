# Get-Command

> 列出当前 PowerShell 会话中可用的命令。
> 此命令只能通过 PowerShell 运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- 列出当前计算机上所有可用的 PowerShell 命令（别名、Cmdlet、函数）：

`Get-Command`

- 列出当前会话中所有可用的 PowerShell 命令：

`Get-Command -ListImported`

- 列出计算机上仅有的 PowerShell 别名/Cmdlet/函数：

`Get-Command -Type {{Alias|Cmdlet|Function}}`

- 列出当前会话中 PATH 上可用的程序或命令：

`Get-Command -Type Application`

- 按模块名称列出仅有的 PowerShell 命令，例如 `Microsoft.PowerShell.Utility` 用于与工具相关的命令：

`Get-Command -Module {{module}}`

- 通过命令名称获取命令信息（例如版本号或模块名称）：

`Get-Command {{command}}`