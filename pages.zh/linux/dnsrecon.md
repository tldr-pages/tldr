# dnsrecon

> DNS 枚举工具。
> 更多信息：<https://github.com/darkoperator/dnsrecon>。

- 扫描一个域并将结果保存到 SQLite 数据库：

`dnsrecon --domain {{example.com}} --db {{path/to/database.sqlite}}`

- 扫描一个域，指定名称服务器并执行区域传输：

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- 扫描一个域，使用暴力攻击和子域名及主机名字典：

`dnsrecon --domain {{example.com}} --dictionary {{path/to/dictionary.txt}} --type brt`

- 扫描一个域，执行 SPF 记录的 IP 范围反向查找并将结果保存到 JSON 文件：

`dnsrecon --domain {{example.com}} -s --json`

- 扫描一个域，执行谷歌枚举并将结果保存到 CSV 文件：

`dnsrecon --domain {{example.com}} -g --csv`

- 扫描一个域，执行 DNS 缓存嗅探：

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{path/to/dictionary.txt}}`

- 扫描一个域，执行区域遍历：

`dnsrecon --domain {{example.com}} --type zonewalk`