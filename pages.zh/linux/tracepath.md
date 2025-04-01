# tracepath

> 跟踪到网络主机的路径，并发现此路径上的 MTU。
> 更多信息：<https://manned.org/tracepath>。

- 跟踪到主机的路径的首选方法：

`tracepath -p {{33434}} {{host}}`

- 指定初始目标端口，对于非标准防火墙设置非常有用：

`tracepath -p {{destination_port}} {{host}}`

- 打印主机名和数值 IP 地址：

`tracepath -b {{host}}`

- 指定最大 TTL（跳数）：

`tracepath -m {{max_hops}} {{host}}`

- 指定初始数据包长度（IPv4 默认为 65535，IPv6 默认为 128000）：

`tracepath -l {{packet_length}} {{host}}`

- 仅使用 IPv6 地址：

`tracepath -6 {{host}}`