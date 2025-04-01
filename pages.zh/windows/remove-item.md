# Remove-Item

> 删除文件、文件夹，以及注册表项和子项。
> 该命令只能通过 PowerShell 运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- 删除特定的文件或注册表项（不包括子项）：

`Remove-Item {{path\to\file_or_key1 , path\to\file_or_key2 ...}}`

- 删除隐藏或只读文件：

`Remove-Item -Force {{path\to\file1 , path\to\file2 ...}}`

- 交互式删除特定的文件或注册表项，在每次删除前提示：

`Remove-Item -Confirm {{path\to\file_or_key1 , path\to\file_or_key2 ...}}`

- 递归删除特定的文件和目录（适用于 Windows 10 版本 1909 及更高版本）：

`Remove-Item -Recurse {{path\to\file_or_directory1 , path\to\file_or_directory2 ...}}`

- 删除特定的 Windows 注册表项及其所有子项：

`Remove-Item -Recurse {{path\to\key1 , path\to\key2 ...}}`

- 执行删除操作的预演：

`Remove-Item -WhatIf {{path\to\file1 , path\to\file2 ...}}`