# gpclient

> 通过 OpenConnect 连接到 Linux 上的 GlobalProtect VPN。
> 更多信息：<https://github.com/yuezk/GlobalProtect-openconnect>。

- 使用门户服务器连接到 GlobalProtect VPN：

`gpclient connect {{vpn_gateway_url}}`

- 断开与当前连接的 VPN 服务器的连接：

`gpclient disconnect`

- 启动用于管理 VPN 的图形用户界面 (GUI)：

`gpclient launch-gui`

- 使用 OpenSSL 解决方案绕过遗留的协商错误：

`gpclient connect --fix-openssl {{vpn_gateway_url}}`

- 连接时忽略 TLS 错误：

`gpclient connect --ignore-tls-errors {{vpn_gateway_url}}`

- 显示版本信息：

`gpclient --version`

- 显示任何命令的帮助信息：

`gpclient help {{command}}`