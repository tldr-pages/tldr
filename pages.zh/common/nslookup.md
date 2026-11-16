# nslookup

> 向名称服务器查询各类域名记录。
> 另请参阅：`dig`, `resolvectl`, `host`。
> 更多信息：<https://manned.org/nslookup>。

- 使用系统默认名称服务器查询域名的 IP 地址（A 记录）：

`nslookup {{example.com}}`

- 向指定名称服务器查询域名的 NS 记录：

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- 查询 IP 地址的反向解析（PTR 记录）：

`nslookup -type=PTR {{54.240.162.118}}`

- 使用 TCP 协议查询任意（ANY）可用记录：

`nslookup -vc -type=ANY {{example.com}}`

- 使用 TCP 协议向指定名称服务器查询整个区域文件（zone transfer）：

`nslookup -vc -type=AXFR {{example.com}} {{名称服务器}}`

- 查询域名的邮件服务器（MX 记录），并显示事务的详细信息：

`nslookup -type=MX -debug {{example.com}}`

- 向指定名称服务器的特定端口查询 TXT 记录：

`nslookup -port={{端口号}} -type=TXT {{example.com}} {{名称服务器}}`
