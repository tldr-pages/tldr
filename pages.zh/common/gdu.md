# gdu

> 带有控制台界面的磁盘使用情况分析器。
> 更多信息：<https://github.com/dundee/gdu>.

- 交互式显示当前目录的磁盘使用情况：

`gdu`

- 交互式显示指定目录的磁盘使用情况：

`gdu {{path/to/directory}}`

- 交互式显示所有已挂载磁盘的磁盘使用情况：

`gdu --show-disks`

- 交互式显示当前目录的磁盘使用情况，但忽略某些子目录：

`gdu --ignore-dirs {{path/to/directory1,path/to/directory2,...}}`

- 通过正则表达式忽略路径：

`gdu --ignore-dirs-pattern '{{.*[abc]+}}'`

- 忽略隐藏目录：

`gdu --no-hidden`

- 仅打印结果，不进入交互模式：

`gdu --non-interactive {{path/to/directory}}`

- 在非交互模式下不显示进度（在脚本中很有用）：

`gdu --no-progress {{path/to/directory}}`
