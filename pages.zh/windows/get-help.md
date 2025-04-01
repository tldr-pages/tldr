# Get-Help

> 显示 PowerShell 命令（别名、cmdlet 和函数）的帮助信息和文档。
> 该命令只能通过 PowerShell 运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- 显示特定 PowerShell 命令的一般帮助信息：

`Get-Help {{command}}`

- 显示特定 PowerShell 命令的详细文档：

`Get-Help {{command}} -Detailed`

- 显示特定 PowerShell 命令的完整技术文档：

`Get-Help {{command}} -Full`

- 打印特定 PowerShell 命令的特定参数的文档（使用 `*` 显示所有参数），如果可用：

`Get-Help {{command}} -Parameter {{parameter}}`

- 打印 cmdlet 的示例，如果可用：

`Get-Help {{command}} -Examples`

- 列出所有可用的 cmdlet 帮助页面：

`Get-Help *`

- 使用 `Update-Help` 更新当前的帮助和文档知识库：

`Update-Help`

- 在默认的 Web 浏览器中查看 PowerShell 命令的在线版本文档：

`Get-Help {{command}} -Online`