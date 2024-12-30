# bluetoothctl

> 管理蓝牙设备。
> 更多信息：<https://bitbucket.org/serkanp/bluetoothctl>。

- 进入 `bluetoothctl` shell：

`bluetoothctl`

- 列出所有已知设备：

`bluetoothctl devices`

- 打开或关闭蓝牙控制器：

`bluetoothctl power {{on|off}}`

- 与设备配对：

`bluetoothctl pair {{mac_address}}`

- 移除设备：

`bluetoothctl remove {{mac_address}}`

- 连接到已配对的设备：

`bluetoothctl connect {{mac_address}}`

- 从已配对的设备断开连接：

`bluetoothctl disconnect {{mac_address}}`

- 显示帮助：

`bluetoothctl help`