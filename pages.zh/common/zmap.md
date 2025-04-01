# zmap

> 快速、开源的网络扫描工具，用于互联网范围的调查。
> 更多信息：<https://github.com/zmap/zmap>.

- 扫描子网或整个IPv4空间的特定TCP端口（默认：80）：

`zmap {{SUBNETS}} -p {{port}}`

- 扫描子网中的特定端口或端口范围：

`zmap {{--target-ports}} {{port1,port2-port3,...}} {{SUBNETS}}`

- 将结果输出到带有自定义字段的CSV文件：

`zmap {{[-o|--output-file]}} {{path/to/output_file.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{SUBNETS}}`

- 将扫描速率限制为每秒特定数量的封包：

`zmap {{[-r|--rate]}} {{packets_per_second}} {{SUBNETS}}`

- 执行一次不发送封包的模拟运行：

`zmap {{[-d|--dryrun]}} {{SUBNETS}}`

- 使用CIDR表示法的黑名单文件排除子网：

`zmap {{[-b|--blocklist-file]}} {{path/to/blocklist.txt}} {{SUBNETS}}`

- 为扫描封包设置特定的源IP地址：

`zmap {{[-S|--source-ip]}} {{source_ip}} {{SUBNETS}}`

- 限制要探测的目标数量或百分比（例如：1000个IP/端口对）：

`zmap {{[-n|--max-targets]}} {{1000}} {{SUBNETS}} {{[-p|--target-ports]}} {{port1,port2-port3}}`