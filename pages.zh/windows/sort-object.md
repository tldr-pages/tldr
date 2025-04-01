# Sort-Object

> 按属性值对对象进行排序。
> 注意：此命令仅能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/sort-object>.

- 按名称对当前目录进行排序：

`Get-ChildItem | Sort-Object`

- 按名称对当前目录进行降序排序：

`Get-ChildItem | Sort-Object -Descending`

- 排序并去除重复项：

`"a", "b", "a" | Sort-Object -Unique`

- 按文件长度对当前目录进行排序：

`Get-ChildItem | Sort-Object -Property Length`

- 按工作集（WS）大小对内存使用最高的进程进行排序：

`Get-Process | Sort-Object -Property WS`