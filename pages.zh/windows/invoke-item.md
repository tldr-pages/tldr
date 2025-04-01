# Invoke-Item

> 在各自的默认程序中打开文件。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- 在默认程序中打开文件：

`Invoke-Item -Path {{path\to\file}}`

- 打开目录中的所有文件：

`Invoke-Item -Path {{path\to\directory}}\*`

- 打开目录中的所有 PNG 文件：

`Invoke-Item -Path {{path\to\directory}}\*.png`

- 打开目录中包含特定关键字的所有文件：

`Invoke-Item -Path {{path\to\directory}}\* -Include {{*keyword*}}`

- 打开目录中除包含特定关键字之外的所有文件：

`Invoke-Item -Path {{path\to\directory}}\* -Exclude {{*keyword*}}`

- 执行预演以确定通过 `Invoke-Item` 将打开哪些文件：

`Invoke-Item -Path {{path\to\directory}}\* -WhatIf`