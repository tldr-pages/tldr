# systemd-socket-activate

> 用于 systemd 服务的套接字激活。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>。

- 当特定套接字连接时激活服务：

`systemd-socket-activate {{path/to/socket.service}}`

- 为服务激活多个套接字：

`systemd-socket-activate {{path/to/socket1.service}} {{path/to/socket2.service}}`

- 向被激活的服务传递环境变量：

`{{SYSTEMD_SOCKET_ACTIVATION=1}} systemd-socket-activate {{path/to/socket.service}}`

- 与通知套接字一起激活服务：

`systemd-socket-activate {{path/to/socket.socket}} {{path/to/service.service}}`

- 激活带有指定端口的服务：

`systemd-socket-activate {{path/to/socket.service}} -l {{8080}}`