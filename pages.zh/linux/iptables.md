# iptables

> 配置 Linux 内核 IPv4 防火墙的表、链和规则。
> 使用 `ip6tables` 设置 IPv6 流量的规则。另见：`iptables-save`，`iptables-restore`。
> 更多信息：<https://manned.org/iptables>。

- 查看过滤表的链、规则、数据包/字节计数器和行号：

`sudo iptables --verbose --numeric --list --line-numbers`

- 设置链 [P]olicy 规则：

`sudo iptables --policy {{chain}} {{rule}}`

- [A]ppend 规则到链策略以适用于 IP：

`sudo iptables --append {{chain}} --source {{ip}} --jump {{rule}}`

- [A]ppend 规则到链策略以适用于 IP，考虑 [p]rotocol 和端口：

`sudo iptables --append {{chain}} --source {{ip}} --protocol {{tcp|udp|icmp|...}} --dport {{port}} --jump {{rule}}`

- 添加一个 NAT 规则，将来自 `192.168.0.0/24` 子网的所有流量转换为主机的公共 IP：

`sudo iptables --table {{nat}} --append {{POSTROUTING}} --source {{192.168.0.0/24}} --jump {{MASQUERADE}}`

- [D]elete 链规则：

`sudo iptables --delete {{chain}} {{rule_line_number}}`