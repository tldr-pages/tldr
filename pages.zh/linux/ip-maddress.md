# ip maddress

> 管理组播地址。
> 更多信息：<https://manned.org/ip-maddress>.

- 列出组播地址及其订阅的程序数量：

`ip {{[m|maddress]}}`

- 列出特定设备的地址：

`ip {{[m|maddress]}} {{[s|show]}} dev {{eth0}}`

- 静态加入一个组播组：

`sudo ip {{[m|maddress]}} {{[a|add]}} {{33:33:00:00:00:02}} dev {{eth0}}`

- 退出一个静态组播组：

`sudo ip {{[m|maddress]}} {{[d|delete]}} {{33:33:00:00:00:02}} dev {{eth0}}`

- 显示帮助：

`ip {{[m|maddress]}} {{[h|help]}}`
