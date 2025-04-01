# dnsmap

> dnsmap 命令用于扫描域名的常见子域名，例如 smtp.domain.org。
> 更多信息：<https://github.com/resurrecting-open-source-projects/dnsmap>。

- 使用内置的字典列表扫描子域名：

`dnsmap {{example.com}}`

- 指定要检查的子域名列表：

`dnsmap {{example.com}} -w {{path/to/wordlist.txt}}`

- 将结果保存到 CSV 文件中：

`dnsmap {{example.com}} -c {{path/to/file.csv}}`

- 忽略 2 个误报的 IP（最多可忽略 5 个）：

`dnsmap {{example.com}} -i {{123.45.67.89,98.76.54.32}}`