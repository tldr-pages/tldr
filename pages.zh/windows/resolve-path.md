# Resolve-Path

> 解析路径中的通配符，并显示路径内容。
> 注意：此命令只能在 PowerShell 中使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- 解析主目录路径：

`Resolve-Path {{~}}`

- 解析 UNC 路径：

`Resolve-Path -Path "\\{{hostname}}\{{path\to\file}}"`

- 获取相对路径：

`Resolve-Path -Path {{path\to\file_or_directory}} -Relative`