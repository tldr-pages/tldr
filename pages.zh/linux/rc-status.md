# rc-status

> 显示关于运行级别的状态信息。
> 另见 `openrc`。
> 更多信息：<https://manned.org/rc-status>。

- 显示服务及其状态的摘要：

`rc-status`

- 在摘要中包含所有运行级别的服务：

`rc-status --all`

- 列出崩溃的服务：

`rc-status --crashed`

- 列出手动启动的服务：

`rc-status --manual`

- 列出受监控的服务：

`rc-status --supervised`

- 获取当前运行级别：

`rc-status --runlevel`

- 列出所有运行级别：

`rc-status --list`