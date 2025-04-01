# bandwhich

> 显示当前按进程、连接或远程 IP/主机名划分的网络使用情况。
> 更多信息：<https://github.com/imsnif/bandwhich>.

- 仅显示远程地址表：

`bandwhich --addresses`

- 显示 DNS 查询：

`bandwhich --show-dns`

- 显示总计（累积）使用量：

`bandwhich --total-utilization`

- 显示特定网络接口的网络使用情况：

`bandwhich --interface {{eth0}}`

- 显示使用指定 DNS 服务器的 DNS 查询：

`bandwhich --show-dns --dns-server {{dns_server_ip}}`
