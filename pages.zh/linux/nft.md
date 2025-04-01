# nft

> 允许配置由 Linux 内核防火墙提供的表、链和规则。
> nftables 取代了 iptables。
> 更多信息：<https://wiki.nftables.org/wiki-nftables/index.php/Main_Page>.

- 查看当前配置：

`sudo nft list ruleset`

- 添加一个新表，表族为 "inet"，表名为 "filter"：

`sudo nft add table {{inet}} {{filter}}`

- 添加一个新链以接受所有入站流量：

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \; \}`

- 添加一条新规则以接受多个 TCP 端口：

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- 添加一条 NAT 规则，将来自 `192.168.0.0/24` 子网的所有流量转换为主机的公网 IP：

`sudo nft add rule {{nat}} {{postrouting}} ip saddr {{192.168.0.0/24}} {{masquerade}}`

- 显示规则句柄：

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- 删除一条规则：

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- 保存当前配置：

`sudo nft list ruleset > {{/etc/nftables.conf}}`