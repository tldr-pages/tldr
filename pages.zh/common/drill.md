# drill

> 执行各种 DNS 查询。
> 更多信息：<https://manned.org/drill>.

- 查询与主机名关联的 IP 地址（A 记录）：

`drill {{example.com}}`

- 查询与给定域名关联的邮件服务器（MX 记录）：

`drill mx {{example.com}}`

- 获取给定域名的所有类型的记录：

`drill any {{example.com}}`

- 指定要查询的备用 DNS 服务器：

`drill {{example.com}} @{{8.8.8.8}}`

- 对 IP 地址执行反向 DNS 查询（PTR 记录）：

`drill -x {{8.8.8.8}}`

- 从根服务器跟踪到域名的 DNSSEC 路径：

`drill -TD {{example.com}}`

- 显示域名的 DNSKEY 记录：

`drill -s dnskey {{example.com}}`
