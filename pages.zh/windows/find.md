# 查找

> 在文件中查找指定字符串。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/find>。

- 查找包含指定字符串的行：

`find "{{string}}" {{path\to\file_or_directory}}`

- 显示不包含指定字符串的行：

`find "{{string}}" {{path\to\file_or_directory}} /v`

- 显示包含指定字符串的行数：

`find "{{string}}" {{path\to\file_or_directory}} /c`

- 显示包含行号的行列表：

`find "{{string}}" {{path\to\file_or_directory}} /n`