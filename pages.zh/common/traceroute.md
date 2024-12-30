# 路由跟踪

> 打印到网络主机的数据包跟踪路线。
> 更多信息：<https://manned.org/traceroute>。

- 跟踪到主机：

`traceroute {{example.com}}`

- 禁用IP地址和主机名映射：

`traceroute -n {{example.com}}`

- 指定响应等待时间（以秒为单位）：

`traceroute --wait={{0.5}} {{example.com}}`

- 指定每跳的查询数量：

`traceroute --queries={{5}} {{example.com}}`

- 指定探测数据包的大小（以字节为单位）：

`traceroute {{example.com}} {{42}}`

- 确定到目标的MTU：

`traceroute --mtu {{example.com}}`

- 使用ICMP而不是UDP进行路由跟踪：

`traceroute --icmp {{example.com}}`