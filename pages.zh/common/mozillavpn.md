# mozillavpn

> 来自 Firefox 制作者的虚拟专用网络。
> 另见：`fastd`，`ivpn`，`mullvad`，`warp-cli`。
> 更多信息：<https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>。

- 使用交互提示登录：

`mozillavpn login`

- 连接到 Mozilla VPN：

`mozillavpn activate`

- 显示连接状态：

`mozillavpn status`

- 列出可用服务器：

`mozillavpn servers`

- 选择特定服务器：

`mozillavpn select {{server_name}}`

- 从 Mozilla VPN 断开连接：

`mozillavpn deactivate`

- 登出：

`mozillavpn logout`

- 显示子命令的帮助：

`mozillavpn {{subcommand}} --help`