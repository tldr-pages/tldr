# ping6

> 使用 IPv6 地址向网络主机发送 ICMP ECHO_REQUEST 数据包。
> 更多信息：<https://manned.org/ping6>.

- 向主机发送 ping 请求：

`ping6 {{host}}`

- 向主机发送特定次数的 ping 请求：

`ping6 -c {{count}} {{host}}`

- 向主机发送 ping 请求，指定请求之间的间隔时间（默认为 1 秒）：

`ping6 -i {{seconds}} {{host}}`

- 不尝试解析地址的符号名称，直接向主机发送 ping 请求：

`ping6 -n {{host}}`

- 向主机发送 ping 请求，并在收到数据包时发出响铃（如果终端支持的话）：

`ping6 -a {{host}}`