# vncviewer

> 启动一个 VNC（虚拟网络计算）客户端。
> 更多信息：<https://manned.org/vncviewer>。

- 启动一个 VNC 客户端并连接到指定显示的主机：

`vncviewer {{host}}:{{display_number}}`

- 以全屏模式启动 VNC 客户端：

`vncviewer -FullScreen {{host}}:{{display_number}}`

- 启动一个具有特定屏幕分辨率的 VNC 客户端：

`vncviewer --geometry {{width}}x{{height}} {{host}}:{{display_number}}`

- 启动一个 VNC 客户端并连接到指定端口的主机：

`vncviewer {{host}}::{{port}}`
