# rc-status

> 显示运行级别状态信息。
> 请参阅 `openrc`。
> 更多信息：<https://manned.org/rc-status>。

- 显示服务及其状态的概要：

`rc-status`

- 在概要中包含所有运行级别中的服务：

`rc-status {{[-a|--all]}}`

- 列出已崩溃的服务：

`rc-status {{[-c|--crashed]}}`

- 列出手动启动的服务：

`rc-status {{[-m|--manual]}}`

- 列出受监督的服务：

`rc-status {{[-S|--supervised]}}`

- 显示当前运行级别：

`rc-status {{[-r|--runlevel]}}`

- 列出所有运行级别：

`rc-status {{[-l|--list]}}`