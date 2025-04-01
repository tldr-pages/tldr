# rc-update

> 在 OpenRC 的运行级别中添加和删除服务。
> 另请参阅 `openrc`。
> 更多信息：<https://manned.org/rc-update>。

- 列出已启用的服务及其添加的运行级别：

`rc-update`

- 列出所有服务：

`rc-update {{[-v|--verbose]}}`

- 向运行级别添加服务：

`sudo rc-update add {{service_name}} {{runlevel}}`

- 从运行级别删除服务：

`sudo rc-update {{[del|delete]}} {{service_name}} {{runlevel}}`

- 从所有运行级别删除服务：

`sudo rc-update {{[-a|--all]}} {{[del|delete]}} {{service_name}}`
