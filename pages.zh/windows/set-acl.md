# Set-Acl

> 更改指定项目（如文件或注册表项）的安全描述符。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- 从一个文件复制安全描述符到另一个文件：

`$OriginAcl = Get-Acl -Path {{path\to\file}}; Set-Acl -Path {{path\to\file}} -AclObject $OriginAcl`

- 使用管道操作符传递描述符：

`Get-Acl -Path {{path\to\file}} | Set-Acl -Path {{path\to\file}}`
