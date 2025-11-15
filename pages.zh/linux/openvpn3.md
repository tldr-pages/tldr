# openvpn3

> OpenVPN 3 Linux 客户端。
> 更多信息：<https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- 打开一个新的 VPN 会话：

`openvpn3 session-start --config {{路径/到/config.conf}}`

- 列出已建立的会话：

`openvpn3 sessions-list`

- 断开当前建立的以给定配置开始的会话：

`openvpn3 session-manage --config {{路径/到/config.conf}} --disconnect`

- 导入 VPN 配置：

`openvpn3 config-import --config {{路径/到/config.conf}}`

- 列出导入的配置：

`openvpn3 configs-list`
