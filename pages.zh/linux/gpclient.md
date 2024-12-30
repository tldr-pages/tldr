# gpclient

> 在Linux上通过OpenConnect连接到GlobalProtect VPN。
> 更多信息：<https://github.com/yuezk/GlobalProtect-openconnect>。

- 使用门户服务器连接到GlobalProtect VPN：

`gpclient connect {{vpn_gateway_url}}`

- 从当前连接的VPN服务器断开连接：

`gpclient disconnect`

- 启动VPN管理的图形用户界面（GUI）：

`gpclient launch-gui`

- 使用OpenSSL解决方法绕过旧版重新协商错误：

`gpclient connect --fix-openssl {{vpn_gateway_url}}`

- 在连接过程中忽略TLS错误：

`gpclient connect --ignore-tls-errors {{vpn_gateway_url}}`

- 显示版本：

`gpclient --version`

- 显示任何命令的帮助：

`gpclient help {{command}}`