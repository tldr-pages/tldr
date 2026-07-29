# arping

> 使用 ARP 协议在网络中探测主机。
> 适用于 MAC 地址发现。
> 更多信息：<https://manned.org/arping>。

- 通过 ARP 请求包 Ping 主机：

`sudo arping {{主机_ip}}`

- 在特定接口上 Ping 主机：

`sudo arping -I {{接口}} {{主机_ip}}`

- Ping 主机并在第一次回复后结束：

`sudo arping -f {{主机_ip}}`

- Ping 主机特定次数：

`sudo arping -c {{次数}} {{主机_ip}}`

- 广播 ARP 请求包以更新邻居的 ARP 缓存（非请求 ARP 模式）：

`sudo arping -U {{要广播的_ip}}`

- 通过发送带有 3 秒超时的 ARP 请求来检测网络中的重复 IP 地址：

`sudo arping -D -w {{3}} {{要检查的_ip}}`
