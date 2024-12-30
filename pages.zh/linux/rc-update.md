# rc-update

> 将 OpenRC 服务添加到和从运行级别中删除。
> 另见 `openrc`。
> 更多信息：<https://manned.org/rc-update>。

- 列出所有服务及其被添加到的运行级别：

`rc-update show`

- 将服务添加到运行级别：

`sudo rc-update add {{service_name}} {{runlevel}}`

- 从运行级别删除服务：

`sudo rc-update delete {{service_name}} {{runlevel}}`

- 从所有运行级别删除服务：

`sudo rc-update --all delete {{service_name}}`