# openvpn3

> OpenVPN 3 Linux 客户端。
> 更多信息：<https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>。

- 启动新的 VPN 会话：

`openvpn3 session-start --config {{path/to/config.conf}}`

- 列出已建立的会话：

`openvpn3 sessions-list`

- 断开当前用给定配置启动的会话：

`openvpn3 session-manage --config {{path/to/config.conf}} --disconnect`

- 导入 VPN 配置：

`openvpn3 config-import --config {{path/to/config.conf}}`

- 列出已导入的配置：

`openvpn3 configs-list`