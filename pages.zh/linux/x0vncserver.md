# x0vncserver

> TigerVNC 服务器用于 X 显示。
> 更多信息：<https://tigervnc.org/doc/x0vncserver.html>。

- 使用密码文件启动 VNC 服务器：

`x0vncserver -display {{:0}} -passwordfile {{path/to/file}}`

- 使用特定端口启动 VNC 服务器：

`x0vncserver -display {{:0}} -rfbport {{port}}`