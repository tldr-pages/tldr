# Move-Item

> 移动或重命名文件、目录、注册表项和其他 PowerShell 数据项。
> 该命令只能在 PowerShell 中运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- 当目标不是现有目录时，重命名文件或目录：

`Move-Item {{path\to\source}} {{path\to\target}}`

- 将文件或目录移动到现有目录中：

`Move-Item {{path\to\source}} {{path\to\existing_directory}}`

- 重命名或移动具有特定名称的文件（不将字符串中的特殊字符视为通配符）：

`Move-Item -LiteralPath "{{path\to\source}}" {{path\to\file_or_directory}}`

- 将多个文件移动到现有目录中，保持文件名不变：

`Move-Item {{path\to\source1 , path\to\source2 ...}} {{path\to\existing_directory}}`

- 移动或重命名注册表项：

`Move-Item {{path\to\source_key1 , path\to\source_key2 ...}} {{path\to\new_or_existing_key}}`

- 在覆盖现有文件或注册表项前不提示确认：

`mv -Force {{path\to\source}} {{path\to\target}}`

- 无论文件权限如何，在覆盖现有文件前提示确认：

`mv -Confirm {{path\to\source}} {{path\to\target}}`

- 在模拟模式下移动文件，显示可以移动的文件和目录，但不实际执行：

`mv -WhatIf {{path\to\source}} {{path\to\target}}`