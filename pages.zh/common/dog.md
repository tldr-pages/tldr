# dog

> DNS 查找工具。
> 它具有多彩的输出，支持 DNS-over-TLS 和 DNS-over-HTTPS 协议，并且可以输出 JSON。
> 更多信息：<https://dns.lookup.dog>。

- 查找与主机名相关联的 IP 地址（A 记录）：

`dog {{example.com}}`

- 查询与给定域名相关联的 MX 记录类型：

`dog {{example.com}} MX`

- 指定要查询的特定 DNS 服务器（例如 Cloudflare）：

`dog {{example.com}} MX @{{1.1.1.1}}`

- 通过 TCP 查询而不是 UDP：

`dog {{example.com}} MX @{{1.1.1.1}} --tcp`

- 使用显式参数通过 TCP 查询与给定域名相关联的 MX 记录类型：

`dog --query {{example.com}} --type MX --nameserver {{1.1.1.1}} --tcp`

- 使用 DNS over HTTPS (DoH) 查找与主机名相关联的 IP 地址（A 记录）：

`dog {{example.com}} --https @{{https://cloudflare-dns.com/dns-query}}`