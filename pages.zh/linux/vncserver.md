# vncserver

> 启动 VNC (Virtual Network Computing) 桌面。
> 更多信息：<https://manned.org/vncserver.1x>。

- 在下一个可用的显示设备上启动 VNC 服务器：

`vncserver`

- 使用特定的屏幕分辨率启动 VNC 服务器：

`vncserver --geometry {{width}}x{{height}}`

- 终止在特定显示设备上运行的 VNC 服务器实例：

`vncserver --kill :{{display_number}}`
