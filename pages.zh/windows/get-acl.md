# Get-Acl

> 获取资源（如文件或注册表键）的安全描述符。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>。

- 显示特定目录的 ACL：

`Get-Acl {{path\to\directory}}`

- 获取注册表键的 ACL：

`Get-Acl -Path {{HKLM:\System\CurrentControlSet\Control}} | Format-List`