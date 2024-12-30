# dnsmap

> dnsmap 命令扫描域名以查找常见子域名，例如 smtp.domain.org。
> 更多信息：<https://github.com/resurrecting-open-source-projects/dnsmap>。

- 使用内部词表扫描子域名：

`dnsmap {{example.com}}`

- 指定要检查的子域名列表：

`dnsmap {{example.com}} -w {{path/to/wordlist.txt}}`

- 将结果存储到 CSV 文件中：

`dnsmap {{example.com}} -c {{path/to/file.csv}}`

- 忽略 2 个假阳性 IP（最多可忽略 5 个）：

`dnsmap {{example.com}} -i {{123.45.67.89,98.76.54.32}}`