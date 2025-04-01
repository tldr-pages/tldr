# telnet

> 使用 telnet 协议连接到主机的指定端口。
> 更多信息：<https://manned.org/telnet>.

- 连接到主机的默认端口：

`telnet {{host}}`

- 连接到主机的指定端口：

`telnet {{ip_address}} {{port}}`

- 退出 telnet 会话：

`quit`

- 发送默认的转义字符组合以终止会话：

`<Ctrl ]>`

- 以 "x" 作为会话终止字符启动 `telnet`：

`telnet -e {{x}} {{ip_address}} {{port}}`

- 连接到 Star Wars 动画：

`telnet {{towel.blinkenlights.nl}}`
