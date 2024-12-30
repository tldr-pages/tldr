# jc

> 将多个命令的输出转换为 JSON。
> 更多信息：<https://github.com/kellyjonbrazil/jc>。

- 通过管道将命令输出转换为 JSON：

`{{ifconfig}} | jc {{--ifconfig}}`

- 通过魔法语法将命令输出转换为 JSON：

`jc {{ifconfig}}`

- 通过管道输出美化的 JSON：

`{{ifconfig}} | jc {{--ifconfig}} -p`

- 通过魔法语法输出美化的 JSON：

`jc -p {{ifconfig}}`