# Get-DedupProperties

> 获取数据去重信息。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- 获取驱动器的数据去重信息：

`Get-DedupProperties -DriveLetter 'C'`

- 使用驱动器标签获取驱动器的数据去重信息：

`Get-DedupProperties -FileSystemLabel 'Label'`

- 使用输入对象获取驱动器的数据去重信息：

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
