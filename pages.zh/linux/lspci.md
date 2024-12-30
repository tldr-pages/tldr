# lspci

> 列出所有PCI设备。
> 更多信息：<https://manned.org/lspci>。

- 显示设备的简要列表：

`lspci`

- 显示更多信息：

`lspci -v`

- 显示处理每个设备的驱动程序和模块：

`lspci -k`

- 显示特定设备：

`lspci -s {{00:18.3}}`

- 以可读的格式输出信息：

`lspci -vm`