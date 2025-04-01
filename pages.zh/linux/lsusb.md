# lsusb

> 显示有关 USB 总线及其连接设备的信息。
> 更多信息：<https://manned.org/lsusb>。

- 列出所有可用的 USB 设备：

`lsusb`

- 以树状结构列出 USB 层次结构：

`lsusb {{[-t|--tree]}}`

- 列出 USB 设备的详细信息：

`lsusb {{[-V|--verbose]}}`

- 列出指定 USB 设备的详细信息：

`lsusb {{[-V|--verbose]}} -s {{bus}}:{{device number}}`

- 列出指定供应商和产品 ID 的设备：

`lsusb -d {{vendor}}:{{product}}`