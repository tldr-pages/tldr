# openrc

> OpenRC 服务管理器。
> 参见：`rc-status`、`rc-update` 和 `rc-service`。
> 更多信息：<https://wiki.gentoo.org/wiki/OpenRC>。

- 切换到特定的运行级别：

`sudo openrc {{runlevel_name}}`

- 切换到特定的运行级别，但不停止任何现有服务：

`sudo openrc {{[-n|--no-stop]}} {{runlevel_name}}`