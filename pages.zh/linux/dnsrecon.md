# dnsrecon

> DNS 枚举工具。
> 更多信息：<https://github.com/darkoperator/dnsrecon>。

- 扫描一个域名并将结果保存到 SQLite 数据库：

`dnsrecon --domain {{example.com}} --db {{path/to/database.sqlite}}`

- 扫描一个域名，指定名称服务器并执行区域传输：

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- 扫描一个域名，使用字典中的子域和主机名进行暴力破解：

`dnsrecon --domain {{example.com}} --dictionary {{path/to/dictionary.txt}} --type brt`

- 扫描一个域名，从 SPF 记录中反查 IP 范围并保存结果到 JSON 文件：

`dnsrecon --domain {{example.com}} -s --json`

- 扫描一个域名，执行 Google 枚举并将结果保存到 CSV 文件：

`dnsrecon --domain {{example.com}} -g --csv`

- 扫描一个域名，执行 DNS 缓存窥探：

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{path/to/dictionary.txt}}`

- 扫描一个域名，执行区域遍历：

`dnsrecon --domain {{example.com}} --type zonewalk`
