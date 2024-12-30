# ip 规则

> IP 路由策略数据库管理。
> 更多信息：<https://manned.org/ip-rule>。

- 显示路由策略：

`ip rule {{show|list}}`

- 基于数据包源地址添加新规则：

`sudo ip rule add from {{192.168.178.2/32}}`

- 基于数据包目的地址添加新规则：

`sudo ip rule add to {{192.168.178.2/32}}`

- 基于数据包源地址删除规则：

`sudo ip rule delete from {{192.168.178.2/32}}`

- 基于数据包目的地址删除规则：

`sudo ip rule delete to {{192.168.178.2/32}}`

- 刷新所有已删除的规则：

`ip rule flush`

- 将所有规则保存到文件：

`ip rule save > {{path/to/ip_rules.dat}}`

- 从文件恢复所有规则：

`ip rule restore < {{path/to/ip_rules.dat}}`