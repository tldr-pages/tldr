# mklink

> 创建符号链接。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>。

- 创建指向文件的符号链接：

`mklink {{路径\到\链接文件}} {{路径\到\源文件}}`

- 创建指向目录的符号链接：

`mklink /d {{路径\到\链接文件}} {{路径\到\源目录}}`

- 创建指向文件的硬链接：

`mklink /h {{路径\到\链接文件}} {{路径\到\源文件}}`

- 创建目录连接：

`mklink /j {{路径\到\链接文件}} {{路径\到\源文件}}`