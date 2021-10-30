# path

> 显示或设置可执行文件的搜索路径。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/path>.

- 显示当前的路径：

`path`

- 将路径设置为一个或多个以分号分隔的目录：

`path {{目录的路径 1[; 目录的路径 2]}}`

- 将新的目录添加到源路径后：

`path {{目录的路径}};%path%`

- 将命令提示符设置为仅搜索当前目录中的可执行文件：

`path ;`
