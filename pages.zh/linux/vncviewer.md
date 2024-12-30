# vncviewer

> 启动 VNC（虚拟网络计算）客户端。
> 更多信息：<https://manned.org/vncviewer>。

- 启动一个连接到指定显示器上的主机的 VNC 客户端：

`vncviewer {{host}}:{{display_number}}`

- 以全屏模式启动：

`vncviewer -FullScreen {{host}}:{{display_number}}`

- 启动一个具有特定屏幕几何形状的 VNC 客户端：

`vncviewer --geometry {{width}}x{{height}} {{host}}:{{display_number}}`

- 启动一个连接到指定端口的主机的 VNC 客户端：

`vncviewer {{host}}::{{port}}`