# envycontrol

> 用于Nvidia Optimus笔记本的GPU切换工具。
> 更多信息：<https://github.com/bayasdev/envycontrol>。

- 在不同的GPU模式之间切换：

`sudo envycontrol -s {{nvidia|integrated|hybrid}}`

- 手动指定显示管理器：

`envycontrol --dm`

- 检查当前GPU模式：

`sudo envycontrol --query`

- 重置设置：

`sudo envycontrol --reset`

- 显示帮助信息：

`envycontrol --help`

- 显示版本：

`envycontrol --version`