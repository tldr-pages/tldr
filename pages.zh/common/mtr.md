# mtr

> Matt 的 Traceroute：综合的 traceroute 和 ping 工具。
> 更多信息：<https://www.bitwizard.nl/mtr/>.

- 对目标主机进行 traceroute 并持续 ping 所有中间跳点：

`mtr {{example.com}}`

- 禁用 IP 地址和主机名映射：

`mtr --no-dns {{example.com}}`

- 每个跳点 ping 10 次后生成输出：

`mtr --report-wide {{example.com}}`

- 强制使用 IPv4 或 IPv6：

`mtr -4 {{example.com}}`

- 在向同一跳点发送另一个数据包之前等待指定的时间（秒）：

`mtr --interval {{10}} {{example.com}}`

- 显示每个跳点的自治系统号 (ASN)：

`mtr --aslookup {{example.com}}`

- 显示 IP 地址和反向 DNS 名称：

`mtr --show-ips {{example.com}}`