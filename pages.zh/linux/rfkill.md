# rfkill

> 启用和禁用无线设备。
> 更多信息：<https://manned.org/rfkill>。

- 列出设备：

`rfkill`

- 按列过滤：

`rfkill -o {{ID,TYPE,DEVICE}}`

- 按类型阻止设备（例如蓝牙、无线局域网）：

`rfkill block {{bluetooth}}`

- 按类型解除阻止设备（例如蓝牙、无线局域网）：

`rfkill unblock {{wlan}}`

- 以JSON格式输出：

`rfkill -J`