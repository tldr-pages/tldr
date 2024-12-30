# ipset

> 为防火墙规则创建 IP 集合。
> 更多信息：<https://manned.org/ipset>。

- 创建一个空的 IP 集合，用于包含 IP 地址：

`ipset create {{set_name}} hash:ip`

- 销毁一个特定的 IP 集合：

`ipset destroy {{set_name}}`

- 将一个 IP 地址添加到特定集合中：

`ipset add {{set_name}} {{192.168.1.25}}`

- 从集合中删除一个特定的 IP 地址：

`ipset del {{set_name}} {{192.168.1.25}}`

- 保存一个 IP 集合：

`ipset save {{set_name}} > {{path/to/ip_set}}`