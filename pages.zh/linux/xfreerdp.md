# xfreerdp

> 自由远程桌面协议实现。
> 更多信息：<https://www.freerdp.com>.

- 连接到 FreeRDP 服务器：

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}}`

- 连接到 FreeRDP 服务器并激活音频输出重定向，使用 `sys:alsa` 设备：

`xfreerdp /u:{{username}} /p:{{password}} /v:{{ip_address}} /sound:{{sys:alsa}}`

- 连接到 FreeRDP 服务器并使用动态分辨率：

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /dynamic-resolution`

- 连接到 FreeRDP 服务器并启用剪贴板重定向：

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} +clipboard`

- 连接到 FreeRDP 服务器并忽略所有证书检查：

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /cert:ignore`

- 连接到 FreeRDP 服务器并共享目录：

`xfreerdp /v:{{ip_address}} /u:{{username}} /p:{{password}} /drive:{{path/to/directory}},{{share_name}}`