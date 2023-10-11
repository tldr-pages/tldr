# airmon-ng

> 激活无线网络设备的监控模式。
> 更多信息：<https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- 列出无线设备和它们的状态：

`sudo airmon-ng`

- 为一个特定的设备打开监控模式：

`sudo airmon-ng start {{wlan0}}`

- 关闭使用无线设备的干扰进程：

`sudo airmon-ng check kill`

- 关闭某个特定网络接口的监控模式：

`sudo airmon-ng stop {{wlan0mon}}`
