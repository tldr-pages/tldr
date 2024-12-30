# arping

> 使用 ARP 协议发现和探测网络中的主机。
> 对于 MAC 地址发现非常有用。
> 更多信息：<https://github.com/ThomasHabets/arping>。

- 通过 ARP 请求数据包 ping 一台主机：

`arping {{host_ip}}`

- 在特定接口上 ping 一台主机：

`arping -I {{interface}} {{host_ip}}`

- 在收到第一个回复后 [f]inish ping 一台主机：

`arping -f {{host_ip}}`

- 对一台主机 ping 指定次数 ([c]ount)：

`arping -c {{count}} {{host_ip}}`

- 广播 ARP 请求数据包以更新邻居的 ARP 缓存 ([U]nsolicited ARP 模式)：

`arping -U {{ip_to_broadcast}}`

- 通过发送 ARP 请求并设置 3 秒超时来 [D]etect 网络中的重复 IP 地址：

`arping -D -w {{3}} {{ip_to_check}}`