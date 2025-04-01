# ufw

> 简单防火墙。
> `iptables` 的前端，旨在使防火墙配置更加容易。
> 更多信息：<https://wiki.ubuntu.com/UncomplicatedFirewall>.

- 启用 ufw:

`ufw enable`

- 禁用 ufw:

`ufw disable`

- 显示 ufw 规则及其编号:

`ufw status numbered`

- 允许进入此主机的 5432 端口流量，并附带注释标识服务:

`ufw allow {{5432}} comment "{{服务}}"`

- 仅允许从 192.168.0.4 到此主机的任何地址的 22 端口的 TCP 流量:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- 拒绝进入此主机的 80 端口流量:

`ufw deny {{80}}`

- 拒绝所有到 8412:8500 端口范围的 UDP 流量:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- 删除特定规则。规则编号可以从 `ufw status numbered` 命令中获取:

`ufw delete {{rule_number}}`