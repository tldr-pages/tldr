# bandwhich

> 显示当前按进程、连接或远程IP/主机名的网络利用率。
> 更多信息：<https://github.com/imsnif/bandwhich>。

- 仅显示远程地址表：

`bandwhich --addresses`

- 显示DNS查询：

`bandwhich --show-dns`

- 显示总（累计）使用情况：

`bandwhich --total-utilization`

- 显示特定网络接口的网络利用率：

`bandwhich --interface {{eth0}}`

- 使用给定的DNS服务器显示DNS查询：

`bandwhich --show-dns --dns-server {{dns_server_ip}}`