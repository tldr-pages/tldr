# adb connect

> 无线连接到 Android 设备。
> 更多信息：<https://developer.android.com/tools/adb>。

- 与 Android 设备配对（地址和配对码可以在开发者选项中找到）：

`adb pair {{ip_address}}:{{port}}`

- 连接到 Android 设备（端口将与配对时不同）：

`adb connect {{ip_address}}:{{port}}`

- 断开设备连接：

`adb disconnect {{ip_address}}:{{port}}`
