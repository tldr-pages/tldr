# dnsx

> 一个快速的多功能 DNS 工具，用于运行多个 DNS 查询。
> 注意：在某些情况下，`dnsx` 的输入需要通过 `stdin`（使用管道 `|`）传递。
> 相关命令：`dig`、`dog`、`dnstracer`。
> 更多信息：<https://github.com/projectdiscovery/dnsx>。

- 查询（子）域的 A 记录并显示收到的响应：

`echo {{example.com}} | dnsx -a {{[-re|-resp]}}`

- 查询所有 DNS 记录（A、AAAA、CNAME、NS、TXT、SRV、PTR、MX、SOA、AXFR、CAA）：

`dnsx -recon {{[-re|-resp]}} <<< {{example.com}}`

- 查询特定类型的 DNS 记录：

`echo {{example.com}} | dnsx {{[-re|-resp]}} -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- 仅输出响应（不显示查询的域或子域）：

`echo {{example.com}} | dnsx {{[-ro|-resp-only]}}`

- 显示查询的原始响应，指定使用的解析器和失败重试次数：

`echo {{example.com}} | dnsx -{{debug|raw}} {{[-r|-resolver]}} {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- 使用占位符暴力破解 DNS 记录：

`dnsx {{[-d|-domain]}} {{FUZZ.example.com}} {{[-w|-wordlist]}} {{path/to/wordlist.txt}} {{[-re|-resp]}}`

- 从域和字典列表中暴力破解 DNS 记录，将输出追加到文件中且不包含颜色代码：

`dnsx {{[-d|-domain]}} {{path/to/domain.txt}} {{[-w|-wordlist]}} {{path/to/wordlist.txt}} {{[-re|-resp]}} {{[-o|-output]}} {{path/to/output.txt}} {{[-nc|-no-color]}}`

- 从给定的子域名列表中提取 `CNAME` 记录，并限制每秒的 DNS 查询速率：

`subfinder -silent {{[-d|-domain]}} {{example.com}} | dnsx -cname {{[-re|-resp]}} {{[-rl|-rate-limit]}} {{number}}`