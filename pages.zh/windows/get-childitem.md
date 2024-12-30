# 获取子项

> 列出目录中的项。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>。

- 列出当前目录中的所有非隐藏项：

`Get-ChildItem`

- 仅列出当前目录中的目录：

`Get-ChildItem -Directory`

- 仅列出当前目录中的文件：

`Get-ChildItem -File`

- 列出当前目录中的项，包括隐藏项：

`Get-ChildItem -Hidden`

- 列出除当前目录外的其他目录中的项：

`Get-ChildItem -Path {{path\to\directory}}`