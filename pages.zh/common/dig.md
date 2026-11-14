# dig

> DNS 查询工具。
> 另请参阅：`resolvectl`, `nslookup`, `host`。
> 更多信息：<https://manned.org/dig>。

- 查询与某主机名关联的 IP 地址（A 记录）：

`dig +short {{example.com}}`

- 获取指定域名的详细应答（A 记录）：

`dig +noall +answer {{example.com}}`

- 查询指定域名下特定类型的 DNS 记录：

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- 指定备用 DNS 服务器进行查询，并可选择使用 DNS over TLS（DoT）：

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- 对 IP 地址执行反向 DNS 查询（PTR 记录）：

`dig -x {{8.8.8.8}}`

- 查找某区域的权威名称服务器并显示 SOA 记录：

`dig +nssearch {{example.com}}`

- 执行迭代查询并显示解析域名的完整追踪路径：

`dig +trace {{example.com}}`

- 使用 TCP 协议在非标准端口（[p]ort）上查询 DNS 服务器：

`dig +tcp -p {{端口}} @{{DNS服务器IP}} {{example.com}}`
