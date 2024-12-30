# ping

> 向网络主机发送 ICMP ECHO_REQUEST 数据包。
> 更多信息：<https://manned.org/ping>。

- Ping 主机：

`ping {{host}}`

- 只对主机进行特定次数的 Ping：

`ping -c {{count}} {{host}}`

- Ping 主机，指定请求之间的间隔时间（默认是 1 秒）：

`ping -i {{seconds}} {{host}}`

- Ping 主机而不尝试查找地址的符号名称：

`ping -n {{host}}`

- Ping 主机并在收到数据包时响铃（如果你的终端支持）：

`ping -a {{host}}`

- 如果没有收到响应，还显示一条消息：

`ping -O {{host}}`

- 使用特定数量的 Ping 对主机进行 Ping，为每个回复设置超时（`-W`）和整个 Ping 运行的总时间限制（`-w`）：

`ping -c {{count}} -W {{seconds}} -w {{seconds}} {{host}}`