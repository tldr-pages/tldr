# kdig

> 高级 DNS 查询工具。
> 更多信息：<https://www.knot-dns.cz/docs/latest/html/man_kdig.html>。

- 查询与主机名关联的 IP 地址（A 记录）：

`kdig {{example.com}}`

- 指定一个特定的 DNS 服务器进行查询（例如 Google DNS）：

`kdig {{example.com}} @{{8.8.8.8}}`

- 查询与给定域名关联的特定 DNS 记录类型：

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- 使用 DNS over TLS (DoT) 查询与主机名关联的 IP 地址（A 记录）：

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} {{example.com}}`

- 使用 DNS over HTTPS (DoH) 查询与主机名关联的 IP 地址（A 记录）：

`kdig -d @{{1.1.1.1}} +https +tls-hostname={{1dot1dot1dot1.cloudflare-dns.com}} {{example.com}}`
