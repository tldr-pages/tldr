# host

> 查找域名服务器。
> 更多信息：<https://manned.org/host>。

- 查找域名的 A、AAAA 和 MX 记录：

`host {{domain}}`

- 查找域名的某个字段（CNAME、TXT 等）：

`host -t {{field}} {{domain}}`

- 反向查找 IP：

`host {{ip_address}}`

- 指定一个备用的 DNS 服务器进行查询：

`host {{domain}} {{8.8.8.8}}`