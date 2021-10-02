# mklink

> 创建符号链接。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/mklink>.

- 创建指向文件的符号链接：

`mklink {{链接文件的路径}} {{源文件路径}}`

- 创建指向目录的符号链接：

`mklink /d {{链接文件的路径}} {{源目录路径}}`

- 创建指向文件的硬链接：

`mklink /h {{链接文件的路径}} {{源目录路径}}`

- 创建目录链接：

`mklink /j {{链接文件的路径}} {{源目录路径}}`
