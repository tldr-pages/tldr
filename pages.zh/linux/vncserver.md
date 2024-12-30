# vncserver

> 启动一个 VNC（虚拟网络计算）桌面。
> 更多信息：<https://manned.org/vncserver.1x>。

- 在下一个可用显示器上启动 VNC 服务器：

`vncserver`

- 使用特定屏幕几何形状启动 VNC 服务器：

`vncserver --geometry {{width}}x{{height}}`

- 杀死运行在特定显示器上的 VNC 服务器实例：

`vncserver --kill :{{display_number}}`