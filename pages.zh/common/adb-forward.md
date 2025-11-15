# adb forward

> 通过无线连接到一个 Android 设备。
> 更多信息：<https://developer.android.com/tools/adb>.

- 转发一个 TCP 端口：

`adb forward tcp:{{本地_端口}} tcp:{{远程_端口}}`

- 列出所有转发规则：

`adb forward --list`

- 移除转发规则：

`adb forward --remove tcp:{{本地_端口}}`

- 移除所有转发规则：

`adb forward --remove-all`
