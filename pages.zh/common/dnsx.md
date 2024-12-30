# dnsx

> 一个快速且多功能的 DNS 工具包，用于运行多个 DNS 查询。
> 注意：在某些情况下，`dnsx` 的输入需要通过 `stdin`（管道 `|`）传递。
> 另请参见：`dig`，`dog`，`dnstracer`。
> 更多信息：<https://github.com/projectdiscovery/dnsx>。

- 查询（子）域名的 A 记录并显示接收到的 [re]sponse：

`echo {{example.com}} | dnsx -a -re`

- 查询所有 DNS 记录（A，AAAA，CNAME，NS，TXT，SRV，PTR，MX，SOA，AXFR，CAA）：

`dnsx -recon -re <<< {{example.com}}`

- 查询特定类型的 DNS 记录：

`echo {{example.com}} | dnsx -re -{{a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa}}`

- 仅输出 [r]esponse [o]nly（不显示查询的域名或子域名）：

`echo {{example.com}} | dnsx -ro`

- 显示查询的原始响应，指定要使用的 [r]esolvers 以及失败时的重试次数：

`echo {{example.com}} | dnsx -{{debug|raw}} -resolver {{1.1.1.1,8.8.8.8,...}} -retry {{number}}`

- 使用占位符进行 DNS 记录的暴力破解：

`dnsx -domain {{FUZZ.example.com}} -wordlist {{path/to/wordlist.txt}} -re`

- 从域名和字典列表进行 DNS 记录的暴力破解，将 [o]utput 附加到没有 [c]olor 代码的文件中：

`dnsx -domain {{path/to/domain.txt}} -wordlist {{path/to/wordlist.txt}} -re -output {{path/to/output.txt}} -no-color`

- 为给定的子域名列表提取 `CNAME` 记录，并对每秒的 DNS 查询进行 [r]ate [l]imiting：

`subfinder -silent -d {{example.com}} | dnsx -cname -re -rl {{number}}`