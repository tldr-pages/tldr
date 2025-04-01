# lychee

> 查找损坏的 URL。
> 更多信息：<https://lychee.cli.rs/usage/cli/>。

- 扫描网站以查找损坏的链接：

`lychee {{https://example.com}}`

- 显示错误类型的详细信息：

`lychee --format detailed {{https://example.com}}`

- 限制连接数量以防止触发 DDOS 防护：

`lychee --max-concurrency {{5}} {{links.txt}}`

- 检查目录结构中的文件是否包含损坏的 URL：

`grep -r "{{pattern}}" | lychee -`

- 显示帮助信息：

`lychee --help`
