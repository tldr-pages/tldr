# New-Item

> 创建新文件、目录、符号链接或注册表项。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- 创建新空白文件（相当于 `touch`）:

`New-Item {{path\to\file}}`

- 创建新目录:

`New-Item -ItemType Directory {{path\to\directory}}`

- 创建带有指定内容的新文本文件:

`New-Item {{path\to\file}} -Value {{content}}`

- 在多个位置创建相同内容的文本文件:

`New-Item {{path\to\file1 , path\to\file2 , ...}} -Value {{content}}`

- 创建指向文件或目录的符号链接、硬链接或连接点:

`New-Item -ItemType {{SymbolicLink|HardLink|Junction}} -Path {{path\to\link_file}} -Target {{path\to\source_file_or_directory}}`

- 创建新空白注册表项（在 REG_SZ 中，使用 `New-ItemProperty` 或 `Set-ItemProperty` 来精调值类型）:

`New-Item {{path\to\registry_key}}`

- 创建带有指定值的新空白注册表项:

`New-Item {{path\to\registry_key}} -Value {{value}}`
