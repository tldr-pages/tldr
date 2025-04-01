# iptables

> 可用于配置 Linux 内核防火墙提供的过滤表、规则链和规则的程序。
> 更多信息：<https://manned.org/iptables>.

- 查看过滤表的规则链、规则以及数据包/字节计数器：

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- 设定规则链策略规则：

`sudo iptables {{[-P|--policy]}} {{规则链}} {{规则}}`

- 追加规则到 IP 的规则链策略：

`sudo iptables {{[-A|--append]}} {{规则链}} {{[-s|--source]}} {{ip}} {{[-j|--jump]}} {{规则}}`

- 追加规则到 IP 的规则链策略（考虑协议与端口）：

`sudo iptables {{[-A|--append]}} {{规则链}} {{[-s|--source]}} {{ip}} {{[-p|--protocol]}} {{协议}} --dport {{端口}} {{[-j|--jump]}} {{规则}}`

- 删除规则链中的规则：

`sudo iptables {{[-D|--delete]}} {{规则链}} {{规则所在行号}}`

- 将指定过滤表的 iptables 配置保存到文件中：

`sudo iptables-save {{[-t|--table]}} {{过滤表名}} > {{iptables_文件路径}}`

- 从文件中还原 iptables 配置：

`sudo iptables-restore < {{iptables_文件路径}}`

