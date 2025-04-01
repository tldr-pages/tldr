# Get-ChildItem

> 列出目录中的项目。
> 注意：此命令仅能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>.

- 列出当前目录中所有非隐藏项目：

`Get-ChildItem`

- 仅列出当前目录中的目录：

`Get-ChildItem -Directory`

- 仅列出当前目录中的文件：

`Get-ChildItem -File`

- 列出当前目录中的项目，包括隐藏项目：

`Get-ChildItem -Hidden`

- 列出其他目录中的项目：

`Get-ChildItem -Path {{path\to\directory}}`