# adb forward

> 无线连接到 Android 设备。
> 更多信息：<https://developer.android.com/tools/adb>。

- 转发 TCP 端口：

`adb forward tcp:{{local_port}} tcp:{{remote_port}}`

- 列出所有转发规则：

`adb forward --list`

- 移除一个转发规则：

`adb forward --remove tcp:{{local_port}}`

- 移除所有转发规则：

`adb forward --remove-all`