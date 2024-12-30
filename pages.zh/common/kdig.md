# kdig

> 高级 DNS 查找工具。
> 更多信息：<https://www.knot-dns.cz/docs/latest/html/man_kdig.html>。

- 查找与主机名关联的 IP 地址（A 记录）：

`kdig {{example.com}}`

- 指定要查询的特定 DNS 服务器（例如 Google DNS）：

`kdig {{example.com}} @{{8.8.8.8}}`

- 查询与给定域名关联的特定 DNS 记录类型：

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- 使用 TLS 进行 DNS 查询以查找与主机名关联的 IP 地址（A 记录）：

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} {{example.com}}`

- 使用 HTTPS 进行 DNS 查询以查找与主机名关联的 IP 地址（A 记录）：

`kdig -d @{{1.1.1.1}} +https +tls-hostname={{1dot1dot1dot1.cloudflare-dns.com}} {{example.com}}`