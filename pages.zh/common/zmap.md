# zmap

> 用于全网范围调查的快速、开源网络扫描器。
> 更多信息：<https://manned.org/zmap>。

- 扫描一个子网或整个 IPv4 地址空间上的指定 TCP 端口（默认：80）：

`zmap {{SUBNETS}} {{[-p|--target-ports]}} {{端口}}`

- 在一个子网中扫描指定的端口或端口范围：

`zmap {{[-p|--target-ports]}} {{端口1, 端口2-端口3,...}} {{SUBNETS}}`

- 将结果输出到包含自定义字段的 CSV 文件中：

`zmap {{[-o|--output-file]}} {{路径/到/输出文件.csv}} {{[-f|--output-fields]}} "{{saddr, daddr, sport, dport}}" {{SUBNETS}}`

- 将扫描速率限制为每秒指定数量的数据包：

`zmap {{[-r|--rate]}} {{每秒数据包数}} {{SUBNETS}}`

- 执行一次不发送任何数据包的空跑：

`zmap {{[-d|--dryrun]}} {{SUBNETS}}`

- 使用 CIDR 表示法的阻止列表文件来排除子网：

`zmap {{[-b|--blocklist-file]}} {{路径/到/阻止列表.txt}} {{SUBNETS}}`

- 为扫描数据包设置指定的源 IP 地址：

`zmap {{[-S|--source-ip]}} {{源_IP}} {{SUBNETS}}`

- 限制要探测的目标数量或百分比（例如 1000 个 IP/端口组合）：

`zmap {{[-n|--max-targets]}} {{1000}} {{SUBNETS}} {{[-p|--target-ports]}} {{端口1, 端口2-端口3}}`
