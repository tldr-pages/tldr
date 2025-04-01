# dog

> DNS 查询工具。
> 它具有彩色输出，支持 DNS-over-TLS 和 DNS-over-HTTPS 协议，并可以输出 JSON。
> 更多信息：<https://dns.lookup.dog>.

- 查询与主机名关联的 IP 地址（A 记录）：

`dog {{example.com}}`

- 查询与给定域名关联的 MX 记录类型：

`dog {{example.com}} MX`

- 指定特定的 DNS 服务器进行查询（例如 Cloudflare）：

`dog {{example.com}} MX @{{1.1.1.1}}`

- 通过 TCP 而不是 UDP 进行查询：

`dog {{example.com}} MX @{{1.1.1.1}} --tcp`

- 使用明确的参数通过 TCP 查询与给定域名关联的 MX 记录类型：

`dog --query {{example.com}} --type MX --nameserver {{1.1.1.1}} --tcp`

- 使用 DNS over HTTPS (DoH) 查询与主机名关联的 IP 地址（A 记录）：

`dog {{example.com}} --https @{{https://cloudflare-dns.com/dns-query}}`
