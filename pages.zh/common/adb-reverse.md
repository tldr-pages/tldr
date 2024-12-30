# adb reverse

> 从连接的 Android 设备或模拟器反向 socket 连接。
> 更多信息：<https://developer.android.com/tools/adb>。

- 列出所有来自模拟器和设备的反向 socket 连接：

`adb reverse --list`

- 从模拟器或设备将 TCP 端口反向到本地主机：

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- 从模拟器或设备移除一个反向 socket 连接：

`adb reverse --remove tcp:{{remote_port}}`

- 从所有模拟器和设备中移除所有反向 socket 连接：

`adb reverse --remove-all`