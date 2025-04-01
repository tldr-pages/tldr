# Get-Content

> 获取指定位置的项目内容。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- 显示文件内容：

`Get-Content -Path {{path\to\file}}`

- 显示文件的前几行：

`Get-Content -Path {{path\to\file}} -TotalCount {{10}}`

- 显示文件内容并持续读取直到按 `<Ctrl c>`：

`Get-Content -Path {{path\to\file}} -Wait`