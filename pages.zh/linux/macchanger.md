# macchanger

> 用于操作网络接口 MAC 地址的命令行工具。
> 更多信息：<https://manned.org/macchanger>.

- 查看接口的当前和永久 MAC 地址：

`macchanger {{[-s|--show]}} {{interface}}`

- 将接口设置为随机的 MAC 地址：

`macchanger {{[-r|--random]}} {{interface}}`

- 将接口设置为随机的 MAC 地址，并假装是 [b]urned-[i]n-[a]ddress：

`macchanger {{[-r|--random]}} {{[-b|--bia]}} {{interface}}`

- 将接口设置为特定的 MAC 地址：

`macchanger {{[-m|--mac]}} {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- 打印所有已知供应商的标识（MAC 地址的前三个字节）：

`macchanger {{[-l|--list]}}`

- 将接口恢复到其永久硬件 MAC 地址：

`macchanger {{[-p|--permanent]}} {{interface}}`
