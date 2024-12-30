# 删除项

> 删除文件、文件夹以及注册表项和子项。
> 此命令只能通过 PowerShell 运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>。

- 删除特定文件或注册表项（不包括子项）：

`Remove-Item {{path\to\file_or_key1 , path\to\file_or_key2 ...}}`

- 删除隐藏或只读文件：

`Remove-Item -Force {{path\to\file1 , path\to\file2 ...}}`

- 交互式提示每次删除前确认删除特定文件或注册表项：

`Remove-Item -Confirm {{path\to\file_or_key1 , path\to\file_or_key2 ...}}`

- 递归删除特定文件和目录（Windows 10 版本 1909 或更高版本）：

`Remove-Item -Recurse {{path\to\file_or_directory1 , path\to\file_or_directory2 ...}}`

- 删除特定 Windows 注册表项及其所有子项：

`Remove-Item -Recurse {{path\to\key1 , path\to\key2 ...}}`

- 执行删除过程的干运行：

`Remove-Item -WhatIf {{path\to\file1 , path\to\file2 ...}}`