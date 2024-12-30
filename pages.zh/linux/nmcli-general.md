# nmcli 一般

> 管理 NetworkManager 的一般设置。
> 此子命令也可以用 `nmcli g` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 显示 NetworkManager 的一般状态：

`nmcli general`

- 显示当前设备的主机名：

`nmcli general hostname`

- 更改当前设备的主机名：

`sudo nmcli general hostname {{new_hostname}}`

- 显示 NetworkManager 的权限：

`nmcli general permissions`

- 显示当前的日志级别和域：

`nmcli general logging`

- 设置日志级别和/或域（有关所有可用域，请参见 `man NetworkManager.conf`）：

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`