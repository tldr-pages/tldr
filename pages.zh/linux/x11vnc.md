# x11vnc

> 一个 VNC 服务器，可以在现有的显示服务器上启用 VNC。
> 默认情况下，服务器会在所有客户端断开连接后自动终止。
> 更多信息：<https://manned.org/x11vnc>。

- 启动一个允许多个客户端连接的 VNC 服务器：

`x11vnc -shared`

- 以只读模式启动 VNC 服务器，并且在最后一个客户端断开连接后不会终止：

`x11vnc -forever -viewonly`

- 在特定的显示和屏幕上启动 VNC 服务器（两者索引均从零开始）：

`x11vnc -display :{{display}}.{{screen}}`

- 在第三个显示的默认屏幕上启动 VNC 服务器：

`x11vnc -display :{{2}}`

- 在第一个显示的第二个屏幕上启动 VNC 服务器：

`x11vnc -display :{{0}}.{{1}}`