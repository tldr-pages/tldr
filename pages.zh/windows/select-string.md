# Select-String

> 在 PowerShell 中查找字符串和文件中的文本。
> 注意：此命令只能通过 PowerShell 使用。
> 您可以使用 `Select-String` 类似于 UNIX 中的 `grep` 或 Windows 中的 `findstr.exe`。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- 在文件中搜索模式：

`Select-String -Path "{{path\to\file}}" -Pattern '{{search_pattern}}'`

- 搜索精确字符串（禁用正则表达式）：

`Select-String -SimpleMatch "{{exact_string}}" {{path\to\file}}`

- 在当前目录中的所有 `.ext` 文件中搜索模式：

`Select-String -Path "{{*.ext}}" -Pattern '{{search_pattern}}'`

- 捕获匹配模式行前后的指定行数：

`Select-String --Context {{2,3}} "{{search_pattern}}" {{path\to\file}}`

- 在 `stdin` 中搜索不匹配模式的行：

`Get-Content {{path\to\file}} | Select-String --NotMatch "{{search_pattern}}"`