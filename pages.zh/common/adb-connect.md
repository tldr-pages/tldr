# adb connect

> 通过无线连接到 Android 设备。
> 更多信息：<https://developer.android.com/tools/adb>.

- 与一个安卓设备配对（可在开发者选项中，找到地址和配对码）：

`adb pair {{ip_地址}}:{{端口}}`

- 与一个安卓设备连接（端口与配对时存在差异）：

`adb connect {{ip_地址}}:{{端口}}`

- 断开与设备的连接：

`adb disconnect {{ip_地址}}:{{端口}}`
