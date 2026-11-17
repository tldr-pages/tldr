# host

> DNS 查询工具。
> 另请参阅：`dig`, `resolvectl`, `nslookup`。
> 更多信息：<https://manned.org/host>。

- 查询域名的 A、AAAA 和 MX 记录：

`host {{域名}}`

- 查询域名的特定类型记录（CNAME、TXT 等）：

`host -t {{记录类型}} {{域名}}`

- 对 IP 地址执行反向查询：

`host {{IP地址}}`

- 指定备用 DNS 服务器进行查询：

`host {{域名}} {{8.8.8.8}}`
