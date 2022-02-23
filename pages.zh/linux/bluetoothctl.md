# bluetoothctl

> 从命令行管理蓝牙设备。
> 更多信息：<https://bitbucket.org/serkanp/bluetoothctl>.

- 进入 bluetoothctl 外壳程序：

`bluetoothctl`

- 列出设备：

`bluetoothctl -- devices`

- 与一个设备配对：

`bluetoothctl -- pair {{mac 地址}}`

- 移除一个设备：

`bluetoothctl -- remove {{mac 地址}}`

- 连接一个已配对的设备：

`bluetoothctl -- connect {{mac 地址}}`

- 断开一个已配对的设备：

`bluetoothctl -- disconnect {{mac 地址}}`
