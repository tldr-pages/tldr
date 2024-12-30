# ledctl

> 英特尔(R) 外壳 LED 控制应用程序。
> 更多信息：<https://manned.org/ledctl>。

- 为指定设备打开 "定位" LED：

`sudo ledctl locate={{/dev/sda,/dev/sdb,...}}`

- 为指定设备关闭 "定位" LED：

`sudo ledctl locate_off={{/dev/sda,/dev/sdb,...}}`

- 为指定设备关闭 "状态" LED 和 "故障" LED：

`sudo ledctl off={{/dev/sda,/dev/sdb,...}}`

- 为指定设备关闭 "状态" LED、"故障" LED 和 "定位" LED：

`sudo ledctl normal={{/dev/sda,/dev/sdb,...}}`