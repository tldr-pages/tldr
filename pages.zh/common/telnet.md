# telnet

> 使用telnet协议连接到主机的指定端口。
> 更多信息：<https://manned.org/telnet>。

- Telnet到主机的默认端口：

`telnet {{host}}`

- Telnet到主机的特定端口：

`telnet {{ip_address}} {{port}}`

- 退出telnet会话：

`quit`

- 发出默认的转义字符组合以终止会话：

`<Ctrl> + ]`

- 以"x"作为会话终止字符启动`telnet`：

`telnet -e {{x}} {{ip_address}} {{port}}`

- Telnet到星际迷航动画：

`telnet {{towel.blinkenlights.nl}}`