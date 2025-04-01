# traceroute

> 打印到网络主机的数据包路由。
> 更多信息：<https://manned.org/traceroute>。

- 跟踪到主机的路由：

`traceroute {{example.com}}`

- 禁用 IP 地址和主机名映射：

`traceroute -n {{example.com}}`

- 指定响应等待时间（秒）：

`traceroute --wait={{0.5}} {{example.com}}`

- 指定每个跃点的查询次数：

`traceroute --queries={{5}} {{example.com}}`

- 指定探测包的大小（字节）：

`traceroute {{example.com}} {{42}}`

- 确定到目标的 MTU：

`traceroute --mtu {{example.com}}`

- 使用 ICMP 而不是 UDP 进行路由跟踪：

`traceroute --icmp {{example.com}}`