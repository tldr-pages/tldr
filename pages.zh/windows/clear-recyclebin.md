# 清空回收站

> 从回收站中清除项目。
> 此命令仅可通过 PowerShell 版本 5.1 及以下或 7.1 及以上使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>。

- 清空并删除回收站内的所有项目：

`Clear-RecycleBin`

- 清空特定驱动器的回收站：

`Clear-RecycleBin -DriveLetter {{C}}`

- 无需进一步确认清空回收站：

`Clear-RecycleBin -Force`