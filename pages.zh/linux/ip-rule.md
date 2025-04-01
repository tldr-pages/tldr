# ip rule

> IP 路由策略数据库管理。
> 更多信息：<https://manned.org/ip-rule>。

- 显示路由策略：

`ip {{[ru|rule]}}`

- 创建优先级高于 `main` 的新通用路由规则：

`sudo ip {{[ru|rule]}} {{[a|add]}} from all lookup {{100}}`

- 基于数据包源地址添加新规则：

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}}`

- 基于数据包目标地址添加新规则：

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}}`

- 删除基于数据包源地址的规则：

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- 删除所有路由规则：

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- 将所有规则保存到文件中：

`ip {{[ru|rule]}} {{[s|save]}} > {{path/to/ip_rules.dat}}`

- 从文件中恢复所有规则：

`sudo ip {{[ru|rule]}} {{[r|restore]}} < {{path/to/ip_rules.dat}}`