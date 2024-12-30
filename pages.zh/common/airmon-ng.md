# airmon-ng

> 在无线网络设备上激活监视模式。
> 是 `aircrack-ng` 的一部分。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=airmon-ng>。

- 列出无线设备及其状态：

`sudo airmon-ng`

- 为特定设备开启监视模式：

`sudo airmon-ng start {{wlan0}}`

- 终止使用无线设备的干扰进程：

`sudo airmon-ng check kill`

- 为特定网络接口关闭监视模式：

`sudo airmon-ng stop {{wlan0mon}}`