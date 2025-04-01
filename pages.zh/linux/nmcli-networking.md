# nmcli networking

> 管理 NetworkManager 的网络状态。
> 此子命令也可以通过 `nmcli n` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 显示 NetworkManager 的网络状态：

`nmcli networking`

- 启用或禁用由 NetworkManager 管理的所有网络和接口：

`nmcli networking {{on|off}}`

- 显示最后已知的连接状态：

`nmcli networking connectivity`

- 显示当前的连接状态：

`nmcli networking connectivity check`
