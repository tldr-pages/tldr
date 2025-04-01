# Clear-RecycleBin

> 清空回收站中的项目。
> 该命令只能在 PowerShell 5.1 及以下版本或 7.1 及以上版本中使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- 清空并删除回收站中的所有项目：

`Clear-RecycleBin`

- 清空特定驱动器的回收站：

`Clear-RecycleBin -DriveLetter {{C}}`

- 清空回收站而不进一步确认：

`Clear-RecycleBin -Force`