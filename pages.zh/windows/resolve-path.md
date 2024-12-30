# 解析路径

> 解析路径中的通配符字符，并显示路径内容。
> 注意：该命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>。

- 解析主文件夹路径：

`Resolve-Path {{~}}`

- 解析 UNC 路径：

`Resolve-Path -Path "\\{{主机名}}\{{文件路径}}"`

- 获取相对路径：

`Resolve-Path -Path {{文件或目录路径}} -Relative`