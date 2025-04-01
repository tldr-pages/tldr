# cli53

> 用于 Amazon Route 53 的命令行工具。
> 更多信息：<https://github.com/barnybug/cli53>.

- 列出域名：

`cli53 list`

- 创建域名：

`cli53 create {{mydomain.com}} --comment "{{comment}}"`

- 导出 bind 区域文件到 `stdout`：

`cli53 export {{mydomain.com}}`

- 创建指向同一区域中相对记录的 `www` 子域名：

`cli53 {{rc|rrcreate}} {{mydomain.com}} {{'www 300 CNAME lb'}}`

- 创建指向外部地址的 `www` 子域名（外部地址必须以点结尾）：

`cli53 {{rc|rrcreate}} {{mydomain.com}} {{'www 300 CNAME lb.externalhost.com.'}}`

- 创建指向 IP 地址的 `www` 子域名：

`cli53 {{rc|rrcreate}} {{mydomain.com}} {{'www 300 A 150.130.110.1'}}`

- 替换指向不同 IP 地址的 `www` 子域名：

`cli53 {{rc|rrcreate}} --replace {{'www 300 A 150.130.110.2'}}`

- 删除 A 记录：

`cli53 {{rd|rrdelete}} {{mydomain.com}} {{www}} {{A}}`