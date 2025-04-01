# Out-String

> 将输入对象输出为字符串。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- 以字符串形式打印主机信息：

`Get-Alias | Out-String`

- 将每个对象转换为字符串，而不是将所有对象连接成一个字符串：

`Get-Alias | Out-String -Stream`

- 使用 `Width` 参数来防止截断：

`@{TestKey = ('x' * 200)} | Out-String -Width {{250}}`
