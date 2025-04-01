# tcptraceroute

> 使用 TCP 数据包实现的 traceroute 工具。
> 更多信息：<https://github.com/mct/tcptraceroute>。

- 跟踪到主机的路由：

`tcptraceroute {{host}}`

- 指定目标端口和数据包长度（以字节为单位）：

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- 指定本地源端口和源地址：

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- 设置第一个和最大 TTL：

`tcptraceroute {{host}} -f {{first_ttl}} -m {{max_ttl}}`

- 指定等待时间和每跳的查询次数：

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- 指定接口：

`tcptraceroute {{host}} -i {{interface}}`
