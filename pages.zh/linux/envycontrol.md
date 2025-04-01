# envycontrol

> 用于 Nvidia Optimus 笔记本的 GPU 切换工具。
> 更多信息：<https://github.com/bayasdev/envycontrol>。

- 切换不同的 GPU 模式：

`sudo envycontrol -s {{nvidia|integrated|hybrid}}`

- 手动指定显示管理器：

`envycontrol --dm`

- 检查当前 GPU 模式：

`sudo envycontrol --query`

- 重置设置：

`sudo envycontrol --reset`

- 显示帮助信息：

`envycontrol --help`

- 显示版本信息：

`envycontrol --version`