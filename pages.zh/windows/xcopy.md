# xcopy

> 复制文件和目录树。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>。

- 将文件复制到指定的目标：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}}`

- 在复制之前列出将要复制的文件：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /p`

- 仅复制目录结构，不包括文件：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /t`

- 复制时包括空目录：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /e`

- 在目标中保留源ACL：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /o`

- 允许在网络连接丢失时恢复：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /z`

- 当目标中存在文件时禁用提示：

`xcopy {{path\to\file_or_directory}} {{path\to\destination_directory}} /y`

- 显示帮助：

`xcopy /?`