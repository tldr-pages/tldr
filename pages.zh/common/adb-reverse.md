# adb reverse

> 安卓调试桥-反射: 反向映射安卓模拟器实例或者已连接的实体设备的套接字连接.
> 更多信息: <https://developer.android.com/studio/command-line/adb>.

- 显示所有来自设备的(DEVICE —> PC)映射的端口连接列表

`adb reverse —list`

- 反向映射端口连接(DEVICE —> PC)

- 将TCP端口从安卓模拟器或设备中映射到localhost:

`adb reverse tcp:{{远程端口}} tcp:{{本地端口}}`

- 从安卓模拟器或设备移除一个反向socket连接:

`adb reverse --remove tcp:{{远程端口}}`

- 从安卓模拟器或设备移除所有反向socket连接:

`adb reverse --remove-all`
