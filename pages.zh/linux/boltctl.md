# boltctl

> 控制雷电设备。
> 更多信息：<https://manned.org/boltctl>。

- 列出连接的（和授权的）设备：

`boltctl`

- 列出连接的设备，包括未授权的设备：

`boltctl list`

- 临时授权设备：

`boltctl authorize {{device_uuid}}`

- 授权并记住设备：

`boltctl enroll {{device_uuid}}`

- 撤销之前授权的设备：

`boltctl forget {{device_uuid}}`

- 显示设备的更多信息：

`boltctl info {{device_uuid}}`