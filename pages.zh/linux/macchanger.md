# macchanger

> 用于操作网络接口 MAC 地址的命令行工具。
> 更多信息：<https://manned.org/macchanger>。

- 查看接口的当前和永久 MAC 地址：

`macchanger --show {{interface}}`

- 将接口设置为随机 MAC：

`macchanger --random {{interface}}`

- 将接口设置为随机 MAC 地址，并假装是一个 [b]urned-[i]n-[a]ddress：

`macchanger --random --bia {{interface}}`

- 将接口设置为特定的 MAC 地址：

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- 打印所有已知厂商的识别码（MAC 地址的前三个字节）：

`macchanger --list`

- 将接口重置为其永久硬件 MAC 地址：

`macchanger --permanent {{interface}}`