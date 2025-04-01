# ipset

> 为防火墙规则创建 IP 集。
> 更多信息：<https://manned.org/ipset>.

- 创建一个空的 IP 集，该集将包含 IP 地址：

`ipset create {{set_name}} hash:ip`

- 销毁特定的 IP 集：

`ipset destroy {{set_name}}`

- 将特定 IP 地址添加到特定集合中：

`ipset add {{set_name}} {{192.168.1.25}}`

- 从集合中删除特定 IP 地址：

`ipset del {{set_name}} {{192.168.1.25}}`

- 保存 IP 集：

`ipset save {{set_name}} > {{path/to/ip_set}}`
