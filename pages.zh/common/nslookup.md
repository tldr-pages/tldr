# nslookup

> 查询各种域记录的名称服务器。
> 更多信息：<https://manned.org/nslookup>。

- 查询系统默认名称服务器以获取域的IP地址（A记录）：

`nslookup {{example.com}}`

- 查询指定名称服务器以获取域的NS记录：

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- 查询IP地址的反向查找（PTR记录）：

`nslookup -type=PTR {{54.240.162.118}}`

- 使用TCP协议查询任何可用记录：

`nslookup -vc -type=ANY {{example.com}}`

- 使用TCP协议查询指定名称服务器的整个区域文件（区域传输）：

`nslookup -vc -type=AXFR {{example.com}} {{name_server}}`

- 查询域的邮件服务器（MX记录），显示交易的详细信息：

`nslookup -type=MX -debug {{example.com}}`

- 在指定端口号上查询指定名称服务器以获取域的TXT记录：

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`