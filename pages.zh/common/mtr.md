# mtr

> Matt的Traceroute：结合了traceroute和ping工具。
> 更多信息：<https://www.bitwizard.nl/mtr/>.

- 对主机进行traceroute并持续ping所有中间跳：

`mtr {{example.com}}`

- 禁用IP地址和主机名映射：

`mtr --no-dns {{example.com}}`

- 在对每个跳进行10次ping后生成输出：

`mtr --report-wide {{example.com}}`

- 强制使用IPv4或IPv6：

`mtr -4 {{example.com}}`

- 在发送另一个数据包到同一跳之前等待给定的时间（以秒为单位）：

`mtr --interval {{10}} {{example.com}}`

- 显示每个跳的自治系统编号（ASN）：

`mtr --aslookup {{example.com}}`

- 显示IP地址和反向DNS名称：

`mtr --show-ips {{example.com}}`