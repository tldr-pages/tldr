# arping

> 使用 ARP 协议在网络中发现并探测主机。
> 可用于发现 MAC 地址。
> 更多信息：<https://manned.org/arping>.

- 通过 ARP 请求数据包 ping 一个主机：

`arping {{主机 IP}}`

- 在指定的 [I] 接口上 ping 一个主机：

`arping -I {{接口}} {{主机 IP}}`

- ping 一个主机，并在收到第一个回复后 [f] 结束：

`arping -f {{主机 IP}}`

- ping 一个主机指定的次数（[c] 次数）：

`arping -c {{次数}} {{主机 IP}}`

- 广播 ARP 请求数据包以更新邻居的 ARP 缓存（[U] 非请求 ARP 模式）：

`arping -U {{要广播的 IP}}`

- 通过发送 ARP 请求并设置 3 秒超时来 [D] 检测网络中重复的 IP 地址：

`arping -D -w {{3}} {{要检查的 IP}}`
