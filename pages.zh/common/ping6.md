# ping6

> 通过IPv6地址向网络主机发送ICMP ECHO_REQUEST数据包。
> 更多信息：<https://manned.org/ping6>。

- Ping一个主机：

`ping6 {{host}}`

- Ping一个主机，仅指定次数：

`ping6 -c {{count}} {{host}}`

- Ping一个主机，指定请求之间的间隔（默认为1秒）：

`ping6 -i {{seconds}} {{host}}`

- Ping一个主机，不尝试查找地址的符号名称：

`ping6 -n {{host}}`

- Ping一个主机，当接收到数据包时发出铃声（如果您的终端支持）：

`ping6 -a {{host}}`