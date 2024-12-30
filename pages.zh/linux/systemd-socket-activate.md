# systemd-socket-activate

> systemd 服务的套接字激活。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>。

- 在特定套接字连接时激活服务：

`systemd-socket-activate {{path/to/socket.service}}`

- 为服务激活多个套接字：

`systemd-socket-activate {{path/to/socket1.service}} {{path/to/socket2.service}}`

- 将环境变量传递给被激活的服务：

`{{SYSTEMD_SOCKET_ACTIVATION=1}} systemd-socket-activate {{path/to/socket.service}}`

- 激活服务并同时激活通知套接字：

`systemd-socket-activate {{path/to/socket.socket}} {{path/to/service.service}}`

- 使用指定端口激活服务：

`systemd-socket-activate {{path/to/socket.service}} -l {{8080}}`