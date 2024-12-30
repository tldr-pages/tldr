# 路径

> 显示或设置可执行文件的搜索路径。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/path>。

- 显示当前路径：

`path`

- 将路径设置为一个或多个用分号分隔的目录：

`path {{path\to\directory1 path\to\directory2 ...}}`

- 将新目录附加到原始路径：

`path {{path\to\directory}};%path%`

- 将命令提示符设置为仅在当前目录中搜索可执行文件：

`path ;`