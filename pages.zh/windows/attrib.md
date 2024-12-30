# attrib

> 显示或更改文件或目录的属性。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>。

- 显示当前目录中所有设置的文件属性：

`attrib`

- 显示特定目录中所有设置的文件属性：

`attrib {{path\to\directory}}`

- 显示当前目录中所有设置的文件和[d]irectory属性：

`attrib /d`

- 显示当前目录及其[s]ub-directory中所有设置的文件属性：

`attrib /s`

- 将`[r]ead-only`或`[a]rchive`或`[s]ystem`或`[h]idden`或`not content [i]ndexed`属性添加到文件或目录：

`attrib +{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`

- 移除文件或目录的特定属性：

`attrib -{{r|a|s|h|i}} {{path\to\file_or_directory1 path\to\file_or_directory2 ...}}`