# lsusb

> 显示有关USB总线及其连接设备的信息。
> 更多信息：<https://manned.org/lsusb>。

- 列出所有可用的USB设备：

`lsusb`

- 以树形结构列出USB层次结构：

`lsusb -t`

- 列出有关USB设备的详细信息：

`lsusb --verbose`

- 列出有关USB设备的详细信息：

`lsusb --verbose -s {{bus}}:{{device number}}`

- 仅列出具有指定供应商和产品ID的设备：

`lsusb -d {{vendor}}:{{product}}`