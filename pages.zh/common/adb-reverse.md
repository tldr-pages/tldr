# adb reverse

> 安卓调试桥-反射： 反向映射安卓模拟器实例或者已连接的实体设备的套接字连接。
> 更多信息：<https://developer.android.com/studio/command-line/adb>.

- 列出所有来自模拟器和设备的映射连接：

`adb reverse --list`

- 将 TCP 端口从安卓模拟器或设备中映射到 localhost：

`adb reverse tcp:{{远程端口}} tcp:{{本地端口}}`

- 从安卓模拟器或设备移除一个反向 socket 连接：

`adb reverse --remove tcp:{{远程端口}}`

- 从安卓模拟器或设备移除所有反向 socket 连接：

`adb reverse --remove-all`
