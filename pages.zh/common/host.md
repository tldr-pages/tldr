# host

> 域名服务器查询。
> 更多信息：<https://manned.org/host>。

- 查询域的 A、AAAA 和 MX 记录：

`host {{domain}}`

- 查询域的指定字段（CNAME、TXT 等）：

`host -t {{field}} {{domain}}`

- 反向查询 IP 地址：

`host {{ip_address}}`

- 指定要查询的备用 DNS 服务器：

`host {{domain}} {{8.8.8.8}}`