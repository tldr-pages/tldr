# x ping

> ping 命令的增强模块。
> 更多信息：<https://x-cmd.com/mod/ping>。

- 默认 ping bing.com：

`x ping`

- ping 指定的主机：

`x ping {{host}}`

- 以热力图形式显示 ping 结果：

`x ping --heatmap {{host}}`

- 以柱状图形式显示 ping 结果：

`x ping --bar {{host}}`

- 处理现有 ping 结果并以热力图显示：

`ping {{host}} | x ping vis --heatmap`

- 显示帮助信息：

`x ping -h`
