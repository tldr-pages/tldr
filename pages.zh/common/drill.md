# drill

> 执行各种 DNS 查询。
> 更多信息：<https://manned.org/drill>。

- 查找与主机名相关联的 IP（A 记录）：

`drill {{example.com}}`

- 查找与给定域名相关联的邮件服务器（MX 记录）：

`drill mx {{example.com}}`

- 获取给定域名的所有类型的记录：

`drill any {{example.com}}`

- 指定一个备用的 DNS 服务器进行查询：

`drill {{example.com}} @{{8.8.8.8}}`

- 对 IP 地址执行反向 DNS 查询（PTR 记录）：

`drill -x {{8.8.8.8}}`

- 从根服务器到域名执行 DNSSEC 跟踪：

`drill -TD {{example.com}}`

- 显示域名的 DNSKEY 记录：

`drill -s dnskey {{example.com}}`