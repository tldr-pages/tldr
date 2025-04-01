# nmcli general

> 管理 NetworkManager 的通用设置。
> 该子命令也可以使用 `nmcli g` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 显示 NetworkManager 的通用状态：

`nmcli general`

- 显示当前设备的主机名：

`nmcli general hostname`

- 更改当前设备的主机名：

`sudo nmcli general hostname {{new_hostname}}`

- 显示 NetworkManager 的权限：

`nmcli general permissions`

- 显示当前的日志级别和域：

`nmcli general logging`

- 设置日志级别和/或域（详见 `man NetworkManager.conf` 以获取所有可用域）：

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`