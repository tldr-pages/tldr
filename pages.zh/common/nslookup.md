# nslookup

> 查询名称服务器以获取各种域名记录。
> 更多信息：<https://manned.org/nslookup>.

- 查询系统默认的名称服务器以获取域名的 IP 地址（A 记录）：

`nslookup {{example.com}}`

- 查询指定的名称服务器以获取域名的 NS 记录：

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- 查询 IP 地址的反向解析（PTR 记录）：

`nslookup -type=PTR {{54.240.162.118}}`

- 使用 TCP 协议查询所有可用记录（ANY 记录）：

`nslookup -vc -type=ANY {{example.com}}`

- 使用 TCP 协议查询指定名称服务器以获取域名的整个区域文件（区域传输）：

`nslookup -vc -type=AXFR {{example.com}} {{name_server}}`

- 查询域名的邮件服务器（MX 记录），显示事务的详细信息：

`nslookup -type=MX -debug {{example.com}}`

- 在指定端口号上查询指定的名称服务器以获取域名的 TXT 记录：

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`