# iw

> 显示和操作无线设备。
> 另见: `iw dev`。
> 更多信息：<https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>。

- 扫描可用的无线网络：

`iw dev {{wlp}} scan`

- 连接到一个开放的无线网络：

`iw dev {{wlp}} connect {{SSID}}`

- 断开当前连接：

`iw dev {{wlp}} disconnect`

- 显示当前连接的信息：

`iw dev {{wlp}} link`

- 列出所有物理和逻辑无线网络接口：

`iw dev`

- 列出所有物理硬件接口的无线功能：

`iw phy`

- 列出内核当前的无线管理域信息：

`iw reg get`

- 显示所有命令的帮助：

`iw help`
