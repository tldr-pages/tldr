# x ping

> ping 命令的增强模块。
> 更多信息：<https://x-cmd.com/mod/ping>。

- ping 指定的主机（省略则默认为 bing.com）：

`x ping {{host}}`

- 以热力图形式显示 ping 结果：

`x ping {{[-m|--heatmap]}} {{host}}`

- 以柱状图形式显示 ping 结果：

`x ping {{[-b|--bar]}} {{host}}`

- 处理现有 ping 结果并以热力图显示：

`ping {{host}} | x ping vis {{[-m|--heatmap]}}`

- 显示帮助：

`x ping {{[-h|--help]}}`
