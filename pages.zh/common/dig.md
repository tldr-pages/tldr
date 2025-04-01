# dig

> DNS 查询工具。
> 更多信息：<https://manned.org/dig>.

- 查询与主机名关联的 IP 地址（A 记录）：

`dig +short {{example.com}}`

- 获取给定域名的详细回答（A 记录）：

`dig +noall +answer {{example.com}}`

- 查询与给定域名关联的特定 DNS 记录类型：

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- 指定要查询的备用 DNS 服务器，并可选地使用 DNS over TLS (DoT)：

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- 对 IP 地址执行反向 DNS 查询（PTR 记录）：

`dig -x {{8.8.8.8}}`

- 查找区域的权威名称服务器并显示 SOA 记录：

`dig +nssearch {{example.com}}`

- 执行迭代查询并显示解析域名的完整跟踪路径：

`dig +trace {{example.com}}`

- 使用 TCP 协议通过非标准 [p] 端口查询 DNS 服务器：

`dig +tcp -p {{port}} @{{dns_server_ip}} {{example.com}}`
