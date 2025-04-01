# arping

> 使用 ARP 协议在网络中发现和探测主机。
> 适用于 MAC 地址发现。
> 更多信息：<https://manned.org/arping>.

- 使用 ARP 请求数据包Ping主机：

`arping {{host_ip}}`

- 在特定接口上Ping主机：

`arping -I {{interface}} {{host_ip}}`

- Ping主机并在收到第一个回复后 [f]结束后：

`arping -f {{host_ip}}`

- 以特定次数 ([c]ount) Ping主机：

`arping -c {{count}} {{host_ip}}`

- 广播 ARP 请求数据包以更新邻居的 ARP 缓存 ([U]nsolicited ARP 模式)：

`arping -U {{ip_to_broadcast}}`

- 通过发送带有 3 秒超时的 ARP 请求 [D]检测网络中的重复 IP 地址：

`arping -D -w {{3}} {{ip_to_check}}`
