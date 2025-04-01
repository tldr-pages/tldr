# mozillavpn

> 由 Firefox 开发者提供的虚拟私有网络。
> 参见: `fastd`, `ivpn`, `mullvad`, `warp-cli`。
> 更多信息: <https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>。

- 通过交互提示登录：

`mozillavpn login`

- 连接到 Mozilla VPN：

`mozillavpn activate`

- 显示连接状态：

`mozillavpn status`

- 列出可用服务器：

`mozillavpn servers`

- 选择特定服务器：

`mozillavpn select {{server_name}}`

- 断开与 Mozilla VPN 的连接：

`mozillavpn deactivate`

- 注销：

`mozillavpn logout`

- 显示子命令的帮助信息：

`mozillavpn {{subcommand}} --help`