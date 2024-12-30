# ufw

> 简易防火墙。
> `iptables` 的前端，旨在简化防火墙的配置。
> 更多信息请访问：<https://wiki.ubuntu.com/UncomplicatedFirewall>。

- 启用 ufw：

`ufw enable`

- 禁用 ufw：

`ufw disable`

- 显示 ufw 规则及其编号：

`ufw status numbered`

- 允许来自本主机端口 5432 的入站流量，并添加服务标识的注释：

`ufw allow {{5432}} comment "{{Service}}"`

- 仅允许来自 192.168.0.4 的 TCP 流量到本主机的任何地址，端口为 22：

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- 拒绝本主机端口 80 的流量：

`ufw deny {{80}}`

- 拒绝所有 UDP 流量到端口范围 8412:8500：

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- 删除特定规则。规则编号可以通过 `ufw status numbered` 命令获取：

`ufw delete {{rule_number}}`