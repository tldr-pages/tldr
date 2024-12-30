# xfreerdp

> 自由远程桌面协议实现。
> 更多信息：<https://www.freerdp.com>。

- 连接到 FreeRDP 服务器：

`xfreerdp /u:{{用户名}} /p:{{密码}} /v:{{IP地址}}`

- 连接到 FreeRDP 服务器并使用 `sys:alsa` 设备激活音频输出重定向：

`xfreerdp /u:{{用户名}} /p:{{密码}} /v:{{IP地址}} /sound:{{sys:alsa}}`

- 以动态分辨率连接到 FreeRDP 服务器：

`xfreerdp /v:{{IP地址}} /u:{{用户名}} /p:{{密码}} /dynamic-resolution`

- 连接到 FreeRDP 服务器并启用剪贴板重定向：

`xfreerdp /v:{{IP地址}} /u:{{用户名}} /p:{{密码}} +clipboard`

- 连接到 FreeRDP 服务器时忽略任何证书检查：

`xfreerdp /v:{{IP地址}} /u:{{用户名}} /p:{{密码}} /cert:ignore`

- 连接到 FreeRDP 服务器并共享目录：

`xfreerdp /v:{{IP地址}} /u:{{用户名}} /p:{{密码}} /drive:{{路径/到/目录}},{{共享名称}}`